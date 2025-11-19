"""Functional tests for WorkflowLogger file operations.

These tests use permanent tracked files in tests/data/functional/logger/
instead of temporary files to follow the project's testing design principles.
"""

from pathlib import Path

import pytest

from causaliq_workflow.logger import LogLevel, WorkflowLogger

# Test data directory
TEST_DATA_DIR = Path(__file__).parent.parent / "data" / "functional" / "logger"


# Test WorkflowLogger with file output configuration
def test_workflow_logger_file_output():
    """WorkflowLogger correctly configures file output with tracked files."""
    log_path = TEST_DATA_DIR / "test_output.log"

    # Clean up from any previous test runs
    if log_path.exists():
        log_path.unlink()

    try:
        logger = WorkflowLogger(log_file=log_path)

        assert logger.log_file == log_path
        assert logger.is_file_logging is True
        assert logger.has_output_destinations is True
        # File should not be opened during initialization (lazy loading)
        assert logger._file_stream is None

        # Trigger lazy file opening
        logger._ensure_file_stream()

        # Now file should be opened and created
        assert logger._file_stream is not None
        assert log_path.exists()

        logger.close()
        assert logger._file_stream is None

    finally:
        # Cleanup after test
        if log_path.exists():
            log_path.unlink()


# Test WorkflowLogger creates parent directories for log file
def test_workflow_logger_creates_directories():
    """WorkflowLogger creates parent directories for log file."""
    log_path = TEST_DATA_DIR / "nested" / "subdir" / "workflow.log"

    # Clean up from any previous test runs
    if log_path.exists():
        log_path.unlink()
    if log_path.parent.exists():
        log_path.parent.rmdir()
    if (
        log_path.parent.parent.exists()
        and log_path.parent.parent.name == "nested"
    ):
        log_path.parent.parent.rmdir()

    try:
        logger = WorkflowLogger(log_file=log_path)

        # Directories should not be created during initialization
        assert not log_path.parent.exists()

        # Trigger lazy file opening - this should create directories
        logger._ensure_file_stream()

        # Verify parent directories were created
        assert log_path.parent.exists()
        assert log_path.parent.is_dir()

        # Verify the log file was created
        assert log_path.exists()

        logger.close()

    finally:
        # Cleanup after test
        if log_path.exists():
            log_path.unlink()
        if log_path.parent.exists():
            log_path.parent.rmdir()
        if (
            log_path.parent.parent.exists()
            and log_path.parent.parent.name == "nested"
        ):
            log_path.parent.parent.rmdir()


# Test WorkflowLogger context manager functionality
def test_workflow_logger_context_manager():
    """WorkflowLogger works as context manager with proper cleanup."""
    log_path = TEST_DATA_DIR / "context_test.log"

    # Clean up from any previous test runs
    if log_path.exists():
        log_path.unlink()

    try:
        with WorkflowLogger(log_file=log_path) as logger:
            # File should not be opened until needed
            assert logger._file_stream is None
            assert logger.is_file_logging is True

            # Trigger file opening
            logger._ensure_file_stream()
            assert logger._file_stream is not None

        # After context exit, stream should be closed
        assert logger._file_stream is None

        # Verify the log file was created
        assert log_path.exists()

    finally:
        # Cleanup after test
        if log_path.exists():
            log_path.unlink()


# Test WorkflowLogger close method is idempotent
def test_workflow_logger_close_idempotent():
    """WorkflowLogger close method can be called multiple times safely."""
    log_path = TEST_DATA_DIR / "close_test.log"

    # Clean up from any previous test runs
    if log_path.exists():
        log_path.unlink()

    try:
        logger = WorkflowLogger(log_file=log_path)

        # Trigger file opening first
        logger._ensure_file_stream()
        assert logger._file_stream is not None

        # Close multiple times should not raise errors
        logger.close()
        logger.close()
        logger.close()

        assert logger._file_stream is None

        # Verify the log file was created
        assert log_path.exists()

    finally:
        # Cleanup after test
        if log_path.exists():
            log_path.unlink()


# Test WorkflowLogger with complex configuration
def test_workflow_logger_complex_configuration():
    """WorkflowLogger handles complex configuration correctly."""
    log_path = TEST_DATA_DIR / "complex_test.log"

    # Clean up from any previous test runs
    if log_path.exists():
        log_path.unlink()

    try:
        logger = WorkflowLogger(
            terminal=True, log_file=log_path, log_level=LogLevel.ALL
        )

        assert logger.terminal is True
        assert logger.log_file == log_path
        assert logger.log_level == LogLevel.ALL
        assert logger.is_terminal_logging is True
        assert logger.is_file_logging is True
        assert logger.has_output_destinations is True

        # File should not be created until needed
        assert logger._file_stream is None
        assert not log_path.exists()

        # Trigger file creation
        logger._ensure_file_stream()

        # Verify the log file was created
        assert log_path.exists()
        assert logger._file_stream is not None

        logger.close()

    finally:
        # Cleanup after test
        if log_path.exists():
            log_path.unlink()


# Test WorkflowLogger file opening error handling
def test_workflow_logger_file_opening_error(monkeypatch):
    """WorkflowLogger handles file opening errors gracefully."""
    # Use a path within test data directory to avoid system permission issues
    log_path = TEST_DATA_DIR / "restricted" / "test.log"

    # Logger creation should succeed (lazy loading)
    logger = WorkflowLogger(log_file=log_path)
    assert logger.log_file == log_path
    assert logger.is_file_logging is True

    # Mock the file opening to simulate permission error
    monkeypatch.setattr(
        "builtins.open",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            PermissionError("Access denied")
        ),
    )

    with pytest.raises(PermissionError):
        logger._ensure_file_stream()


# Test WorkflowLogger with existing log file (append behavior)
def test_workflow_logger_append_to_existing_file():
    """WorkflowLogger appends to existing log files."""
    log_path = TEST_DATA_DIR / "existing.log"

    # Ensure test data file exists (create if missing for CI)
    if not log_path.exists():
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(
            "# Existing log file for logger functional tests\n"
            "# This file should be preserved across test runs\n"
            "Initial log content\n"
        )

    # Verify the existing test file has content
    assert log_path.exists()
    original_content = log_path.read_text()
    assert "Initial log content" in original_content

    try:
        # Create logger with existing file
        logger = WorkflowLogger(log_file=log_path)

        assert logger.is_file_logging is True
        # File should not be opened until needed
        assert logger._file_stream is None

        # Trigger file opening (should open in append mode)
        logger._ensure_file_stream()
        assert logger._file_stream is not None

        logger.close()

        # Verify original content is preserved (file opened in append mode)
        final_content = log_path.read_text()
        assert "Initial log content" in final_content

    finally:
        # Restore original content
        log_path.write_text(original_content)


# Test _ensure_file_stream is idempotent
def test_ensure_file_stream_idempotent():
    """_ensure_file_stream can be called multiple times safely."""
    log_path = TEST_DATA_DIR / "idempotent_test.log"

    # Clean up from any previous test runs
    if log_path.exists():
        log_path.unlink()

    try:
        logger = WorkflowLogger(log_file=log_path)

        # Call multiple times - should not error
        logger._ensure_file_stream()
        first_stream = logger._file_stream

        logger._ensure_file_stream()
        second_stream = logger._file_stream

        # Should be the same stream object
        assert first_stream is second_stream
        assert log_path.exists()

        logger.close()

    finally:
        # Cleanup after test
        if log_path.exists():
            log_path.unlink()
