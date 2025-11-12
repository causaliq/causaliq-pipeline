"""Unit tests for schema validation - no filesystem access."""

from unittest.mock import patch

import pytest

from causaliq_pipeline.schema import WorkflowValidationError, validate_workflow


# Test WorkflowValidationError exception creation
def test_error_with_message_only():
    """Test creating error with message only."""
    error = WorkflowValidationError("Test error")
    assert str(error) == "Test error"
    assert error.schema_path == ""


# Test WorkflowValidationError with schema path
def test_error_with_schema_path():
    """Test creating error with schema path information."""
    error = WorkflowValidationError(
        "Validation failed", schema_path="steps[0].run"
    )
    assert str(error) == "Validation failed"
    assert error.schema_path == "steps[0].run"


# Test workflow validation with valid workflow data
def test_valid_workflow():
    """Test validating a properly structured workflow."""
    valid_workflow = {
        "name": "Test Workflow",
        "steps": [{"run": "echo hello"}, {"uses": "action@v1"}],
    }
    result = validate_workflow(valid_workflow)
    assert result is True


# Test workflow validation missing name field
def test_missing_name_field():
    """Test validation fails when required name field missing."""
    invalid_workflow = {"steps": [{"run": "echo hello"}]}
    with pytest.raises(WorkflowValidationError) as exc_info:
        validate_workflow(invalid_workflow)
    assert "validation failed" in str(exc_info.value).lower()


# Test workflow validation missing steps field
def test_missing_steps_field():
    """Test validation fails when required steps field missing."""
    invalid_workflow = {"name": "Test Workflow"}
    with pytest.raises(WorkflowValidationError) as exc_info:
        validate_workflow(invalid_workflow)
    assert "validation failed" in str(exc_info.value).lower()


# Test workflow validation with empty steps array
def test_empty_steps_array():
    """Test validation fails when steps array is empty."""
    invalid_workflow = {"name": "Test Workflow", "steps": []}
    with pytest.raises(WorkflowValidationError) as exc_info:
        validate_workflow(invalid_workflow)
    assert "validation failed" in str(exc_info.value).lower()


# Test workflow validation with invalid step structure
def test_step_missing_run_and_uses():
    """Test validation fails when step has neither run nor uses."""
    invalid_workflow = {
        "name": "Test Workflow",
        "steps": [{"name": "Invalid step"}],
    }
    with pytest.raises(WorkflowValidationError) as exc_info:
        validate_workflow(invalid_workflow)
    assert "validation failed" in str(exc_info.value).lower()


# Test workflow validation when jsonschema import fails
def test_missing_jsonschema_import():
    """Test validation fails gracefully when jsonschema not available."""
    valid_workflow = {
        "name": "Test Workflow",
        "steps": [{"run": "echo hello"}],
    }

    # Mock import to raise ImportError
    with patch.dict("sys.modules", {"jsonschema": None}):
        with pytest.raises(WorkflowValidationError) as exc_info:
            validate_workflow(valid_workflow)
        assert "jsonschema library required" in str(exc_info.value)
