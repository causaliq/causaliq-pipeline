"""Unit tests for WorkflowLogger core structure.

These tests focus on in-memory behavior and configuration without file I/O.
File-based operations are tested in tests/functional/test_logger.py.
"""

import sys
from pathlib import Path

import pytest

from causaliq_workflow.logger import LogLevel, WorkflowLogger


# Test LogLevel enum has all expected values
def test_log_level_enum_values():
    """LogLevel enum defines all expected verbosity levels."""
    expected_levels = {"none", "summary", "all"}
    actual_levels = {level.value for level in LogLevel}
    assert actual_levels == expected_levels


# Test LogLevel enum values match names as strings
def test_log_level_string_values():
    """LogLevel enum values match their names in lowercase."""
    for level in LogLevel:
        assert level.value == level.name.lower()


# Test WorkflowLogger instantiation with default parameters
def test_workflow_logger_default_initialization():
    """WorkflowLogger initializes with correct default values."""
    logger = WorkflowLogger()

    assert logger.terminal is True
    assert logger.log_file is None
    assert logger.log_level == LogLevel.SUMMARY
    assert logger.is_terminal_logging is True
    assert logger.is_file_logging is False
    assert logger.has_output_destinations is True


# Test WorkflowLogger with terminal disabled
def test_workflow_logger_terminal_disabled():
    """WorkflowLogger correctly handles terminal output disabled."""
    logger = WorkflowLogger(terminal=False)

    assert logger.terminal is False
    assert logger.is_terminal_logging is False
    assert logger.has_output_destinations is False


# Test WorkflowLogger file configuration without actual file operations
def test_workflow_logger_file_configuration():
    """WorkflowLogger correctly stores file configuration without
    opening files."""
    log_path = Path("test.log")

    # Test configuration storage without file operations
    logger = WorkflowLogger(log_file=log_path, terminal=False)

    assert logger.log_file == log_path
    assert logger.is_file_logging is True
    assert logger.has_output_destinations is True
    # File should not be opened during initialization
    assert logger._file_stream is None


# Test WorkflowLogger with all log levels
@pytest.mark.parametrize(
    "log_level", [LogLevel.NONE, LogLevel.SUMMARY, LogLevel.ALL]
)
def test_workflow_logger_log_levels(log_level):
    """WorkflowLogger accepts all valid log levels."""
    logger = WorkflowLogger(log_level=log_level)

    assert logger.log_level == log_level


# Test WorkflowLogger context manager interface
def test_workflow_logger_context_manager_interface():
    """WorkflowLogger implements context manager protocol."""
    logger = WorkflowLogger(terminal=False)

    # Test context manager methods exist
    assert hasattr(logger, "__enter__")
    assert hasattr(logger, "__exit__")

    # Test context manager returns self
    with logger as ctx_logger:
        assert ctx_logger is logger


# Test WorkflowLogger with both terminal and file disabled
def test_workflow_logger_no_output_destinations():
    """WorkflowLogger handles case with no output destinations."""
    logger = WorkflowLogger(terminal=False, log_file=None)

    assert logger.is_terminal_logging is False
    assert logger.is_file_logging is False
    assert logger.has_output_destinations is False


# Test WorkflowLogger file stream properties when file not specified
def test_workflow_logger_no_file_stream():
    """WorkflowLogger file stream properties when no file specified."""
    logger = WorkflowLogger(log_file=None)

    assert logger._file_stream is None
    assert logger.is_file_logging is False


# Test WorkflowLogger close method is idempotent
def test_workflow_logger_close_idempotent():
    """WorkflowLogger close method can be called multiple times safely."""
    logger = WorkflowLogger(terminal=False)

    # Close multiple times should not raise errors
    logger.close()
    logger.close()
    logger.close()

    # Method should be callable without error
    assert True  # Test passes if no exception raised


# Test WorkflowLogger terminal stream initialization
def test_workflow_logger_terminal_stream():
    """WorkflowLogger initializes terminal stream correctly."""
    logger = WorkflowLogger()

    assert logger._terminal_stream is sys.stdout


# Test WorkflowLogger with complex configuration
def test_workflow_logger_complex_configuration():
    """WorkflowLogger handles complex configuration correctly."""
    log_path = Path("workflow.log")

    logger = WorkflowLogger(
        terminal=True, log_file=log_path, log_level=LogLevel.ALL
    )

    assert logger.terminal is True
    assert logger.log_file == log_path
    assert logger.log_level == LogLevel.ALL
    assert logger.is_terminal_logging is True
    assert logger.is_file_logging is True
    assert logger.has_output_destinations is True
    # File should not be opened during initialization
    assert logger._file_stream is None
