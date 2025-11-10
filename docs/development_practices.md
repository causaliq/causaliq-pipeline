# CausalIQ Pipeline - Development Practices

This document outlines development practices specific to **causaliq-pipeline**. For ecosystem-wide standards, see the [main CausalIQ contributing guide](https://github.com/causaliq/causaliq/blob/main/CONTRIBUTING.md).

## Pipeline-Specific Standards

### Orchestration Code Quality
Beyond the standard CausalIQ requirements:
- **Workflow Validation**: All YAML schemas must have comprehensive validation
- **DASK Integration**: All parallel components must handle DASK futures properly
- **Package Coordination**: Integration with other CausalIQ packages must be robust
- **Resource Management**: Memory and compute allocation must be configurable

### Pipeline Architecture Patterns

#### 1. YAML-First Design
- All functionality must be expressible through YAML configuration
- Configuration validation before execution
- Clear error messages for configuration issues
- Support for templating and parameter substitution

#### 2. CausalIQ Package Integration
- Use CausalIQRegistry for package discovery
- Follow standardized CausalIQ interfaces
- Handle package availability gracefully
- Support version compatibility checking

#### 3. DASK-Native Implementation
- Build DASK task graphs, don't just submit functions
- Optimize for data locality and minimal transfers
- Support both local and distributed execution
- Implement proper resource cleanup

## Testing Strategy for Pipeline

### Pipeline-Specific Test Structure
```
tests/
├── unit/
│   ├── test_yaml_parser.py      # Configuration parsing
│   ├── test_task_graph.py       # DASK graph generation
│   └── test_package_registry.py # Package integration
├── functional/
│   ├── test_workflow_execution.py # End-to-end workflows
│   └── test_llm_coordination.py   # LLM integration
└── integration/
    ├── test_causaliq_discovery.py # Real package tests
    └── test_dask_cluster.py       # Distributed execution
```

### Testing Requirements
- **Workflow Tests**: Test complete YAML workflows end-to-end
- **Package Mocking**: Mock CausalIQ packages for unit tests
- **DASK Testing**: Test both local and distributed execution
- **Configuration Testing**: Validate all YAML schema combinations

## Pipeline-Specific Architecture Principles

### 1. Configuration Transparency
- Users should understand execution from YAML alone
- Provide dry-run capabilities for workflow validation
- Generate execution plans that are human-readable

### 2. Package Agnostic Design
- Don't hardcode assumptions about specific packages
- Support dynamic package discovery and loading
- Handle package evolution and version differences

### 3. Scalability Patterns
- Design for both single-machine and cluster execution
- Support streaming and batch processing modes
- Implement adaptive resource allocation

## Development Workflow for Pipeline

### Branch Strategy (Pipeline-Specific)
- `feature/yaml-*`: YAML configuration features
- `feature/dask-*`: DASK integration improvements  
- `feature/integration-*`: Package integration work
- `feature/llm-*`: LLM coordination features

### Pipeline Testing Requirements
```powershell
# Full pipeline test suite
.\scripts\check_ci.ps1

# Test with specific CausalIQ packages
python -m pytest tests/integration/ -k "discovery"

# Test DASK integration
python -m pytest tests/integration/test_dask_cluster.py

# Validate YAML schemas
python -m pytest tests/unit/test_yaml_parser.py -v
```

## Dependencies Specific to Pipeline

### Core Orchestration Dependencies
- **DASK[complete]**: For distributed execution
- **PyYAML**: For configuration parsing
- **jsonschema**: For YAML validation
- **networkx**: For dependency graph management

### CausalIQ Integration Dependencies
- **importlib-metadata**: For package discovery
- **packaging**: For version compatibility
- **typing-extensions**: For advanced type hints

### Optional Dependencies by Feature
```toml
[project.optional-dependencies]
llm = ["causaliq-llm"]
discovery = ["causaliq-discovery"] 
analysis = ["causaliq-analysis"]
score = ["causaliq-score"]
cluster = ["dask-kubernetes", "dask-yarn"]
```

## Documentation Standards for Pipeline

### Pipeline-Specific Documentation
- **Workflow Examples**: Comprehensive YAML examples
- **Package Integration Guide**: How to integrate new CausalIQ packages
- **DASK Optimization Guide**: Performance tuning for causal algorithms
- **Troubleshooting Guide**: Common orchestration issues

### User Documentation Requirements
- Every YAML configuration option must be documented
- Include performance guidance for different algorithms
- Provide migration guides for workflow updates
- Document resource requirements for different scales

## Performance Considerations for Pipeline

### Orchestration Efficiency
- Minimize overhead in workflow coordination
- Optimize YAML parsing and validation
- Cache package discovery and method introspection
- Efficient dependency resolution algorithms

### DASK Optimization Patterns
- Batch similar operations for efficiency
- Minimize data serialization between tasks
- Use appropriate DASK collections (bag, dataframe, array)
- Implement custom graph optimizations for causal algorithms

### Memory Management for Causal Workflows
- Support out-of-core processing for large datasets
- Implement intelligent caching strategies
- Provide memory usage estimation for workflows
- Support graceful degradation when memory limited

## Security for Pipeline Orchestration

### Workflow Security
- Validate all user-provided YAML configurations
- Sandbox package execution when possible
- Implement resource limits for workflows
- Audit logging for workflow execution

### Package Integration Security
- Verify package signatures when available
- Implement package capability restrictions
- Provide isolated execution environments
- Monitor resource usage during execution

This document should be used alongside the main CausalIQ development standards for comprehensive pipeline development guidance.