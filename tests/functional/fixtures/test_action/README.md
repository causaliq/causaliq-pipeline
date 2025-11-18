# Test Action Package

Example external action package for causaliq-workflow that demonstrates the zero-configuration plugin pattern.

## Installation

```bash
pip install test_action
```

## Usage

After installation, simply import and use in workflows:

```python
import test_action  # This makes the action available
```

```yaml
# workflow.yml
id: example-workflow
steps:
  - name: "Run Test Action"
    uses: "test_action"
    with:
      data_path: "/data/input.csv"
      output_dir: "/results"
      message: "Custom test message"
```

## Key Features

- **Zero Configuration**: No entry points or config files needed
- **Standard Interface**: Follows causaliq-workflow Action conventions
- **Plug-and-Play**: Just import and use immediately
- **Type Safety**: Full type hints and validation

## How It Works

The package exports a class named `Action` that inherits from `causaliq_workflow.action.Action`. 
When imported, causaliq-workflow automatically discovers and registers it.

## Action Specification

- **Name**: test-action
- **Inputs**: data_path (required), output_dir (required), message (optional)  
- **Outputs**: output_file, message_count, status
- **Modes**: dry-run, run, compare