"""
Unit tests for causaliq_workflow.action module.

Tests the base Action class, ActionInput dataclass, and exceptions.
"""

import typing

import pytest

from causaliq_workflow.action import (
    Action,
    ActionExecutionError,
    ActionInput,
    ActionValidationError,
)


# Test ActionInput can be created with all parameters
def test_action_input_creation():
    action_input = ActionInput(
        name="test_param",
        description="A test parameter",
        required=True,
        default="default_value",
        type_hint="str",
    )

    assert action_input.name == "test_param"
    assert action_input.description == "A test parameter"
    assert action_input.required is True
    assert action_input.default == "default_value"
    assert action_input.type_hint == "str"


# Test ActionInput default values
def test_action_input_defaults():
    action_input = ActionInput(
        name="minimal_param",
        description="Minimal parameter",
    )

    assert action_input.name == "minimal_param"
    assert action_input.description == "Minimal parameter"
    assert action_input.required is False
    assert action_input.default is None
    assert action_input.type_hint == "Any"


# Test ActionExecutionError can be created and raised
def test_action_execution_error_creation():
    with pytest.raises(ActionExecutionError, match="Test execution error"):
        raise ActionExecutionError("Test execution error")


# Test ActionExecutionError inherits from Exception
def test_action_execution_error_inheritance():
    error = ActionExecutionError("test")
    assert isinstance(error, Exception)


# Test ActionValidationError can be created and raised
def test_action_validation_error_creation():
    with pytest.raises(ActionValidationError, match="Test validation error"):
        raise ActionValidationError("Test validation error")


# Test ActionValidationError inherits from Exception
def test_action_validation_error_inheritance():
    error = ActionValidationError("test")
    assert isinstance(error, Exception)


class ConcreteTestAction(Action):
    """Concrete Action implementation for testing base class."""

    name = "test-concrete-action"
    version = "1.0.0"
    description = "Test concrete action"

    def run(self, inputs: dict, **kwargs) -> dict:
        """Test implementation of run method."""
        return {"status": "success", "inputs_received": inputs}


# Test concrete Action can be instantiated
def test_concrete_action_instantiation():
    action = ConcreteTestAction()
    assert action.name == "test-concrete-action"
    assert action.version == "1.0.0"
    assert action.description == "Test concrete action"


# Test concrete Action run method
def test_concrete_action_run():
    action = ConcreteTestAction()
    inputs = {"param1": "value1", "param2": "value2"}

    result = action.run(inputs)

    assert result["status"] == "success"
    assert result["inputs_received"] == inputs


# Test default validate_inputs returns True
def test_validate_inputs_default_implementation():
    action = ConcreteTestAction()
    inputs = {"any": "inputs"}

    result = action.validate_inputs(inputs)

    assert result is True


# Test that Action abstract class cannot be instantiated directly
def test_action_cannot_be_instantiated_directly():
    with pytest.raises(
        TypeError, match="Can't instantiate abstract class Action"
    ):
        Action()  # type: ignore


# Test that WorkflowContext is available for type hints
def test_workflow_context_type_hint_import():
    # This test ensures the TYPE_CHECKING import path is covered
    if typing.TYPE_CHECKING:
        from causaliq_workflow.registry import WorkflowContext  # type: ignore

        assert WorkflowContext is not None

    # Verify the import doesn't happen at runtime
    import causaliq_workflow.action as action_module

    assert not hasattr(action_module, "WorkflowContext")


# Test that TYPE_CHECKING block is properly covered
def test_action_module_type_checking_coverage():
    # Import the action module to trigger TYPE_CHECKING evaluation
    import causaliq_workflow.action

    # Verify that during static type checking, WorkflowContext would be
    # available but at runtime it's not imported into the module namespace
    action_module = causaliq_workflow.action
    assert hasattr(action_module, "Action")
    assert hasattr(action_module, "ActionInput")
    assert hasattr(action_module, "ActionExecutionError")
    assert hasattr(action_module, "ActionValidationError")

    # WorkflowContext should not be in the runtime namespace
    assert not hasattr(action_module, "WorkflowContext")
