"""
Workflow execution engine for CausalIQ Workflow.

Provides parsing and execution of GitHub Actions-style YAML workflows with
matrix strategy support for causal discovery experiments.
"""

import itertools
import re
from pathlib import Path
from typing import Any, Dict, List, Set, Union

from causaliq_workflow.schema import (
    WorkflowValidationError,
    load_workflow_file,
    validate_workflow,
)


class WorkflowExecutionError(Exception):
    """Raised when workflow execution fails."""

    pass


class WorkflowExecutor:
    """Parse and execute GitHub Actions-style workflows with matrix expansion.

    This class handles the parsing of YAML workflow files and expansion of
    matrix strategies into individual experiment jobs. It provides the
    foundation for executing multi-step causal discovery workflows with
    parameterised experiments using flexible action parameter templating.
    """

    def parse_workflow(
        self, workflow_path: Union[str, Path]
    ) -> Dict[str, Any]:
        """Parse workflow YAML file with validation.

        Args:
            workflow_path: Path to workflow YAML file

        Returns:
            Parsed and validated workflow dictionary

        Raises:
            WorkflowExecutionError: If workflow parsing or validation fails
        """
        try:
            workflow = load_workflow_file(workflow_path)
            validate_workflow(workflow)
            self._validate_template_variables(workflow)
            return workflow
        except WorkflowValidationError as e:
            raise WorkflowExecutionError(
                f"Workflow validation failed: {e}"
            ) from e

    def expand_matrix(
        self, matrix: Dict[str, List[Any]]
    ) -> List[Dict[str, Any]]:
        """Expand matrix variables into individual job configurations.

        Generates all combinations from matrix variables using cartesian
        product. Each combination becomes a separate job configuration.

        Args:
            matrix: Dictionary mapping variable names to lists of values

        Returns:
            List of job configurations with matrix variables expanded

        Raises:
            WorkflowExecutionError: If matrix expansion fails
        """
        if not matrix:
            return [{}]

        try:
            # Get variable names and value lists
            variables = list(matrix.keys())
            value_lists = list(matrix.values())

            # Generate cartesian product of all combinations
            combinations = list(itertools.product(*value_lists))

            # Create job configurations
            jobs = []
            for combination in combinations:
                job = dict(zip(variables, combination))
                jobs.append(job)

            return jobs

        except Exception as e:
            raise WorkflowExecutionError(
                f"Matrix expansion failed: {e}"
            ) from e

    def _extract_template_variables(self, text: Any) -> Set[str]:
        """Extract template variables from a string.

        Finds all {{variable}} patterns and returns variable names.

        Args:
            text: String that may contain {{variable}} patterns

        Returns:
            Set of variable names found in templates
        """
        if not isinstance(text, str):
            return set()

        # Pattern matches {{variable_name}} with alphanumeric, _, -
        pattern = r"\{\{([a-zA-Z_][a-zA-Z0-9_-]*)\}\}"
        matches = re.findall(pattern, text)
        return set(matches)

    def _validate_template_variables(self, workflow: Dict[str, Any]) -> None:
        """Validate that all template variables in workflow exist in context.

        Args:
            workflow: Parsed workflow dictionary

        Raises:
            WorkflowExecutionError: If unknown template variables found
        """
        # Build available context
        available_variables = {"id", "description"}

        # Add matrix variables if present
        if "matrix" in workflow:
            available_variables.update(workflow["matrix"].keys())

        # Collect all template variables used in workflow
        used_variables: Set[str] = set()
        self._collect_template_variables(workflow, used_variables)

        # Check for unknown variables
        unknown_variables = used_variables - available_variables
        if unknown_variables:
            unknown_list = sorted(unknown_variables)
            available_list = sorted(available_variables)
            raise WorkflowExecutionError(
                f"Unknown template variables: {unknown_list}. "
                f"Available variables: {available_list}"
            )

    def _collect_template_variables(
        self, obj: Any, used_variables: Set[str]
    ) -> None:
        """Recursively collect template variables from workflow object.

        Args:
            obj: Workflow object (dict, list, or string) to scan
            used_variables: Set to collect found variables into
        """
        if isinstance(obj, dict):
            for value in obj.values():
                self._collect_template_variables(value, used_variables)
        elif isinstance(obj, list):
            for item in obj:
                self._collect_template_variables(item, used_variables)
        elif isinstance(obj, str):
            used_variables.update(self._extract_template_variables(obj))
