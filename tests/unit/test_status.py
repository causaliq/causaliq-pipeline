"""Tests for TaskStatus enum."""

import pytest

from causaliq_workflow import TaskStatus
from causaliq_workflow.status import TaskStatus as DirectTaskStatus


# Test package-level imports work correctly
def test_package_root_import():
    """TaskStatus is available from causaliq_workflow package."""
    assert TaskStatus is not None
    assert TaskStatus == DirectTaskStatus


# Test enum values can be accessed through package import
def test_enum_accessible_from_package():
    """Enum values accessible through package import."""
    assert TaskStatus.EXECUTES.value == "EXECUTES"
    assert TaskStatus.FAILED.value == "FAILED"


# Verify all 10 expected status values are defined in the enum
def test_all_status_values_defined():
    """All 10 expected status values are defined."""
    expected_statuses = {
        "EXECUTES",
        "WOULD_EXECUTE",
        "SKIPS",
        "WOULD_SKIP",
        "IDENTICAL",
        "DIFFERENT",
        "INVALID_USES",
        "INVALID_PARAMETER",
        "FAILED",
        "TIMED_OUT",
    }
    actual_statuses = {status.value for status in TaskStatus}
    assert actual_statuses == expected_statuses


# Ensure enum values match their names as strings
def test_status_string_values():
    """Enum values match their names as strings."""
    for status in TaskStatus:
        assert status.value == status.name


# Test is_success property correctly identifies successful execution statuses
def test_is_success_property():
    """is_success property identifies successful statuses."""
    success_statuses = {
        TaskStatus.EXECUTES,
        TaskStatus.WOULD_EXECUTE,
        TaskStatus.SKIPS,
        TaskStatus.WOULD_SKIP,
        TaskStatus.IDENTICAL,
        TaskStatus.DIFFERENT,
    }

    for status in TaskStatus:
        if status in success_statuses:
            assert status.is_success, f"{status} should be success"
        else:
            assert not status.is_success, f"{status} should not be success"


# Test is_error property correctly identifies error conditions
def test_is_error_property():
    """is_error property identifies error statuses."""
    error_statuses = {
        TaskStatus.INVALID_USES,
        TaskStatus.INVALID_PARAMETER,
        TaskStatus.FAILED,
        TaskStatus.TIMED_OUT,
    }

    for status in TaskStatus:
        if status in error_statuses:
            assert status.is_error, f"{status} should be error"
        else:
            assert not status.is_error, f"{status} should not be error"


# Test is_execution property identifies statuses where execution occurred
def test_is_execution_property():
    """is_execution property identifies actual execution."""
    execution_statuses = {
        TaskStatus.EXECUTES,
        TaskStatus.IDENTICAL,
        TaskStatus.DIFFERENT,
    }

    for status in TaskStatus:
        if status in execution_statuses:
            assert status.is_execution, f"{status} should be execution"
        else:
            assert not status.is_execution, f"{status} not execution"


# Test is_dry_run property identifies dry-run mode specific statuses
def test_is_dry_run_property():
    """is_dry_run property identifies dry-run statuses."""
    dry_run_statuses = {TaskStatus.WOULD_EXECUTE, TaskStatus.WOULD_SKIP}

    for status in TaskStatus:
        if status in dry_run_statuses:
            assert status.is_dry_run, f"{status} should be dry-run"
        else:
            assert not status.is_dry_run, f"{status} should not be dry-run"


# Verify each status has exactly one primary property (success or error)
def test_status_properties_mutually_exclusive():
    """Status properties are properly categorized."""
    for status in TaskStatus:
        # Count how many properties are True
        property_count = sum(
            [
                status.is_success,
                status.is_error,
            ]
        )

        # Each status should have exactly one primary property
        # (success or error, but not both or neither)
        assert property_count == 1, f"{status} has {property_count} properties"


# Ensure enum covers all documented status categories completely
def test_enum_completeness():
    """Enum covers all documented status categories."""
    # Core execution statuses
    core_execution = {
        TaskStatus.EXECUTES,
        TaskStatus.WOULD_EXECUTE,
        TaskStatus.SKIPS,
        TaskStatus.WOULD_SKIP,
    }

    # Compare mode statuses
    compare_statuses = {TaskStatus.IDENTICAL, TaskStatus.DIFFERENT}

    # Error statuses
    error_statuses = {
        TaskStatus.INVALID_USES,
        TaskStatus.INVALID_PARAMETER,
        TaskStatus.FAILED,
        TaskStatus.TIMED_OUT,
    }

    all_documented = core_execution | compare_statuses | error_statuses
    all_enum_values = set(TaskStatus)

    assert all_documented == all_enum_values


# Verify TaskStatus class has appropriate documentation
def test_status_documentation_present():
    """All status categories are documented in class docstring."""
    assert "Execution:" in TaskStatus.__doc__
    assert "Comparison:" in TaskStatus.__doc__
    assert "Errors:" in TaskStatus.__doc__


# Test each individual status value is correctly defined with parametrized test
@pytest.mark.parametrize(
    "status_name,expected_value",
    [
        ("EXECUTES", "EXECUTES"),
        ("WOULD_EXECUTE", "WOULD_EXECUTE"),
        ("SKIPS", "SKIPS"),
        ("WOULD_SKIP", "WOULD_SKIP"),
        ("IDENTICAL", "IDENTICAL"),
        ("DIFFERENT", "DIFFERENT"),
        ("INVALID_USES", "INVALID_USES"),
        ("INVALID_PARAMETER", "INVALID_PARAMETER"),
        ("FAILED", "FAILED"),
        ("TIMED_OUT", "TIMED_OUT"),
    ],
)
def test_individual_status_values(status_name, expected_value):
    """Individual status values are correctly defined."""
    status = getattr(TaskStatus, status_name)
    assert status.value == expected_value
    assert status.name == status_name


# Verify enum iteration behavior is consistent and complete
def test_enum_iteration_order():
    """Enum values can be iterated consistently."""
    status_names = [status.name for status in TaskStatus]

    # Should have all 10 statuses
    assert len(status_names) == 10

    # Should be able to iterate multiple times with same order
    second_iteration = [status.name for status in TaskStatus]
    assert status_names == second_iteration


# Test enum membership, equality, and string comparison operations
def test_enum_membership():
    """Enum membership and equality work correctly."""
    # Test membership
    assert TaskStatus.EXECUTES in TaskStatus

    # Test equality
    assert TaskStatus.EXECUTES == TaskStatus.EXECUTES
    assert TaskStatus.EXECUTES != TaskStatus.FAILED

    # Test string comparison
    assert TaskStatus.EXECUTES.value == "EXECUTES"
