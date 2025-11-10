# CausalIQ Pipeline - LLM Communication Guide

This document provides **pipeline-specific guidance** for communicating with LLMs when working on causaliq-pipeline. For general CausalIQ ecosystem communication patterns, see the [main CausalIQ repo](https://github.com/causaliq/causaliq).

## Essential Context for Pipeline Work

### 1. Pipeline Position in Ecosystem
Always start conversations with:
```
I'm working on causaliq-pipeline, the workflow orchestration capability within the CausalIQ ecosystem. This package coordinates causal discovery experiments using DASK and YAML configuration, focusing on a "series" concept for organizing experiments across datasets, algorithms, and parameters.

Current focus: Three-month development plan for basic framework and research support
Ecosystem context: https://causaliq.org/projects/ecosystem_architecture/  
Ecosystem development standards: https://github.com/causaliq/causaliq/blob/main/LLM_DEVELOPMENT_GUIDE.md
Three-month roadmap: docs/development_roadmap.md
Technical architecture: docs/technical_architecture_focused.md
```

### 2. Key Implementation Priorities (3 Month Focus)
For current development work:
```
Current implementation priorities:
1. YAML configuration system with inheritance and validation
2. Series concept for experiment organization across datasets/algorithms
3. DASK integration for parallel execution of causal discovery
4. External package plugins (R bnlearn, Java Tetrad)
5. Dataset download/randomization via zenodo-sync
6. Pause/resume workflow functionality
7. LLM integration hooks for May 2026 research (model averaging)

Migration context: Gradual transition from monolithic discovery repo to modular ecosystem
Research deadline: May 2026 paper on LLM integration for intelligent model averaging
```
For orchestration-specific discussions:
```
The pipeline architecture focuses on:
- DASK task graph generation from YAML workflows
- CausalIQ package coordination and integration
- Resource management for parallel causal discovery
- LLM workflow enhancement coordination

See docs/technical_architecture.md for component details.
```

## Pipeline-Specific Communication Patterns

### For Workflow Orchestration Features
```
I need to implement [ORCHESTRATION_FEATURE] for causaliq-pipeline.

Requirements:
- Coordinate with CausalIQ packages: [list specific packages]
- Generate DASK task graph from YAML configuration
- Handle parallel execution of causal algorithms
- Integrate with causaliq-llm for workflow enhancement
- Follow CausalIQ ecosystem standards

Technical details:
- YAML workflow schema: [specific requirements]
- DASK integration points: [specific needs]
- Package coordination: [how packages interact]

Reference: docs/example_workflows.md for usage scenarios
```

### For YAML Configuration Design
```
I need to design YAML configuration for [WORKFLOW_TYPE] in causaliq-pipeline.

Context:
- Workflow coordinates: [list CausalIQ packages involved]
- Execution pattern: [parallel/sequential/mixed]
- Resource requirements: [DASK scaling needs]
- LLM integration points: [where causaliq-llm fits]

Requirements:
- Intuitive syntax for researchers
- Support for package method specification
- Dependency management between steps
- Resource allocation directives

See docs/example_workflows.md for existing patterns.
```

### For Package Integration
```
I need to integrate [CAUSALIQ_PACKAGE] with causaliq-pipeline orchestration.

Integration requirements:
- Follow CausalIQPackage interface pattern
- Support method discovery and execution
- Handle CausalData format standardization
- Enable YAML workflow configuration
- Coordinate with DASK task execution

Package context: [specific package capabilities]
Workflow context: [how it fits in orchestration]

Reference: docs/technical_architecture_focused.md CausalIQ integration section
```

### For DASK Optimization
```
I need to optimize DASK execution for [CAUSAL_ALGORITHM_TYPE] in causaliq-pipeline.

Context:
- Algorithm characteristics: [computational profile]
- Data requirements: [memory/storage needs]  
- Parallelization potential: [how to split work]
- Integration with other causal algorithms: [workflow context]

Optimization goals:
- Efficient resource utilization
- Minimize data transfer between workers
- Optimize for causal discovery algorithm patterns
- Support dynamic scaling

Reference: docs/technical_architecture_focused.md TaskGraphBuilder section
```

## Pipeline-Specific Context Files

### Always Reference for Pipeline Work
1. `docs/technical_architecture_focused.md` - Pipeline orchestration components
2. `docs/example_workflows.md` - YAML workflow patterns  
3. `docs/development_roadmap.md` - Three-month implementation plan
4. Main `README.md` - Project overview and quick start

### Reference from Main CausalIQ Repo
5. [CausalIQ README](https://github.com/causaliq/causaliq) - Ecosystem overview
6. [CausalIQ CONTRIBUTING](https://github.com/causaliq/causaliq/blob/main/CONTRIBUTING.md) - Development standards

## Specific Prompt Patterns for Pipeline

### For Workflow Engine Development
```
Implement [COMPONENT] for causaliq-pipeline WorkflowEngine.

Requirements:
- Process YAML workflow configurations
- Generate optimized DASK task graphs for causal discovery
- Coordinate execution across CausalIQ packages
- Handle errors and provide detailed logging
- Support interactive and batch execution modes

Integration points:
- CausalIQRegistry for package discovery
- TaskGraphBuilder for DASK coordination
- LLMWorkflowCoordinator for enhancement

Follow the interface patterns in docs/technical_architecture_focused.md
```

### For YAML Schema Design
```
Design YAML schema for [WORKFLOW_TYPE] in causaliq-pipeline.

Schema requirements:
- Express dependencies between causal discovery steps
- Specify CausalIQ package methods and parameters
- Define parallel execution branches
- Include LLM integration points
- Support resource allocation directives

User experience goals:
- Intuitive for causal discovery researchers
- Reusable across different datasets
- Extensible for new CausalIQ packages

Reference existing patterns in docs/example_workflows.md
```

### For Testing Pipeline Components
```
Create tests for [PIPELINE_COMPONENT] in causaliq-pipeline.

Test requirements:
- Unit tests: Mock CausalIQ package interactions
- Functional tests: End-to-end workflow execution
- Integration tests: Real package coordination with DASK
- Performance tests: Scaling and resource utilization

Test scenarios:
- YAML configuration validation
- DASK task graph generation
- Package method execution coordination
- Error handling and recovery

Follow CausalIQ testing standards and existing patterns in tests/
```

## Anti-Patterns for Pipeline Work

### ❌ Generic Orchestration Requests
```
"Help me with workflow orchestration"
```

### ✅ Pipeline-Specific Requests  
```
"Implement YAML-to-DASK task graph generation for coordinating causaliq-discovery algorithms in parallel, following our CausalIQRegistry pattern"
```

### ❌ Isolated Component Design
```
"Create a standalone YAML parser"
```

### ✅ Ecosystem-Integrated Design
```
"Create YAML parser for causaliq-pipeline that validates CausalIQ package methods and generates DASK-compatible execution plans"
```

## Quick Reference Template

```
## Pipeline Context
Working on: causaliq-pipeline (orchestration for CausalIQ ecosystem)
Architecture: docs/technical_architecture_focused.md
Workflows: docs/example_workflows.md
Ecosystem: https://github.com/causaliq/causaliq
Roadmap: docs/development_roadmap.md

## Current Task
Orchestration focus: [YAML/DASK/Package coordination]
CausalIQ packages involved: [discovery/analysis/llm/score]
Workflow type: [research/production/interactive]
Development phase: [Month 1/2/3 from roadmap]

## Specific Request
[Detailed orchestration requirements with ecosystem context]

## Expected Integration
- DASK task graph: [how it should execute]
- Package coordination: [how packages interact]  
- YAML configuration: [how users configure it]
```

This guide ensures effective LLM communication specifically for pipeline orchestration while leveraging the broader CausalIQ ecosystem context.

## Effective Communication Patterns

### For Feature Development
```
I need to implement [FEATURE] for causaliq-pipeline. This should:
- Integrate with our YAML workflow configuration system
- Work with DASK for parallel execution  
- Follow our plugin architecture pattern
- Include comprehensive tests and documentation
- Support the example workflows in docs/example_workflows.md

Technical requirements:
- [Specific technical details]
- [Performance requirements]
- [Integration points]

Please provide implementation following our architecture patterns.
```

### For Debugging/Issues
```
I'm encountering [ISSUE] in causaliq-pipeline. 

Context:
- Component: [WorkflowEngine/PackageRegistry/etc.]
- Workflow: [Link to specific workflow or config]
- Error: [Full error message and stack trace]
- Environment: [Python version, OS, DASK version]

Expected behavior: [What should happen]
Actual behavior: [What is happening]

Our architecture uses [relevant architectural pattern]. How should I debug and fix this?
```

### For Architecture Decisions
```
I need to make an architecture decision for causaliq-pipeline regarding [DECISION].

Options considered:
1. [Option 1 with pros/cons]
2. [Option 2 with pros/cons]

Constraints:
- Must work with our YAML configuration system
- Needs DASK integration
- Should support plugin architecture
- Must maintain backward compatibility

Our current architecture (docs/technical_architecture.md) uses [relevant patterns]. What's the best approach given our design principles?
```

### For Code Review
```
Please review this code for causaliq-pipeline component [COMPONENT].

Requirements checklist:
- [ ] Follows type hints standard
- [ ] Includes Google-style docstrings  
- [ ] Has comprehensive tests (unit/functional/integration)
- [ ] Integrates properly with workflow engine
- [ ] Supports YAML configuration
- [ ] Handles errors gracefully
- [ ] Includes appropriate logging

Code:
[CODE BLOCK]

Please check against our development practices and architecture patterns.
```

## Context Files to Reference

### Always Include
1. `docs/project_blueprint.md` - Overall project vision and goals
2. `docs/technical_architecture.md` - Technical implementation details
3. `docs/development_practices.md` - Coding standards and practices

### Include When Relevant
4. `docs/example_workflows.md` - Workflow examples and use cases
5. `pyproject.toml` - Dependencies and project configuration
6. `src/causaliq_pipeline/` - Current implementation
7. `tests/` - Existing test patterns

## Specific Prompt Patterns

### For New Components
```
Create a new [COMPONENT] for causaliq-pipeline that [PURPOSE].

Requirements:
- Implement the interface defined in docs/technical_architecture.md
- Follow the plugin architecture pattern
- Support YAML configuration
- Include DASK integration where applicable
- Follow development practices in docs/development_practices.md

The component should integrate with:
- [List specific integration points]

Example usage scenarios:
- [Reference specific workflows from docs/example_workflows.md]
```

### For Testing
```
Create comprehensive tests for [COMPONENT] in causaliq-pipeline.

Test requirements:
- Unit tests: Mock external dependencies, test core logic
- Functional tests: Test component behavior end-to-end  
- Integration tests: Test interaction with DASK/other packages
- Achieve 90% code coverage minimum
- Follow existing test patterns in tests/ directory

Component interface: [Reference from technical_architecture.md]
Usage scenarios: [Reference from example_workflows.md]
```

### For Documentation
```
Create/update documentation for [COMPONENT/FEATURE] in causaliq-pipeline.

Documentation should include:
- Clear purpose and use cases
- Integration with overall architecture
- Configuration options (YAML format)
- Code examples matching our API patterns
- Usage in workflow context

Target audiences:
- Developers integrating with the pipeline
- Researchers creating workflows  
- DevOps teams deploying pipelines

Follow the style and structure of existing docs/ files.
```

## Anti-Patterns to Avoid

### ❌ Vague Requests
```
"Help me with causal discovery"
```

### ✅ Specific Requests  
```
"Implement the PC algorithm integration for causaliq-pipeline following our PackageRegistry pattern, with YAML configuration support and DASK parallelization"
```

### ❌ Generic Solutions
```
"Here's a general DASK example..."
```

### ✅ Project-Specific Solutions
```
"Here's how to implement this in causaliq-pipeline's TaskGraphBuilder, integrating with your WorkflowEngine and YAML configuration system..."
```

## Maintaining Context Across Conversations

### Session Continuity
```
Continuing work on causaliq-pipeline [COMPONENT]. Previous context:
- Implemented: [What was done]
- Current focus: [What we're working on]
- Next steps: [What's planned]

Architecture references: [Relevant docs sections]
```

### Progress Tracking
```
Progress update on causaliq-pipeline [FEATURE]:

Completed:
- [X] Component A (following technical_architecture.md)
- [X] Tests achieving 95% coverage
- [X] YAML configuration support

In Progress:
- [ ] DASK integration
- [ ] Documentation updates

Blocked/Questions:
- [Issue description with context]
```

## Quick Reference Template

Save this template for consistent LLM communication:

```
## Project Context
Working on: causaliq-pipeline (workflow orchestration for causal discovery/inference)
Architecture: docs/technical_architecture.md
Standards: docs/development_practices.md  
Examples: docs/example_workflows.md

## Current Task
[Specific task description]

## Requirements
- Component: [Which architectural component]
- Integration: [DASK/YAML/LLM/Package registry]
- Standards: [Type hints, tests, docs, error handling]

## Specific Question/Request
[Detailed description with context]

## Expected Outcome
[What should be delivered]
```

This guide ensures maximum LLM effectiveness by providing clear context, specific requirements, and consistent communication patterns aligned with your project's architecture and standards.

## Development Practices (Short-Term Solo Development)

*Since this will be solo development for the next six months, development practices are integrated into this LLM communication guide for efficiency.*

### Pipeline-Specific Standards for LLM Discussions

When discussing development practices with LLMs, include these pipeline-specific requirements:

#### Orchestration Code Quality
```
For causaliq-pipeline development, ensure:
- Workflow Validation: All YAML schemas must have comprehensive validation
- DASK Integration: All parallel components must handle DASK futures properly  
- Package Coordination: Integration with other CausalIQ packages must be robust
- Resource Management: Memory and compute allocation must be configurable
```

#### Architecture Pattern Context
```
Pipeline follows these patterns (reference when discussing design):
1. YAML-First Design: All functionality expressible through YAML
2. CausalIQ Package Integration: Use CausalIQRegistry for discovery
3. DASK-Native Implementation: Build task graphs, not just submit functions

See docs/technical_architecture.md for full component details.
```

#### Testing Context for LLM Discussions
```
When implementing features, follow this test structure:
- Unit tests: YAML parsing, DASK graph generation, package registry
- Functional tests: End-to-end workflows, LLM coordination  
- Integration tests: Real package tests, distributed execution

Testing command: .\scripts\check_ci.ps1
```

#### Dependencies for Implementation Discussions
```
Core orchestration dependencies:
- DASK[complete]: For distributed execution
- PyYAML: For configuration parsing
- jsonschema: For YAML validation
- networkx: For dependency graph management

Optional by feature: llm, discovery, analysis, cluster extensions
```

#### Performance Considerations for LLM Code Reviews
```
When reviewing implementations, consider:
- Orchestration Efficiency: Minimize workflow coordination overhead
- DASK Optimization: Batch operations, minimize serialization
- Memory Management: Support out-of-core processing for large datasets
- Resource Limits: Implement workflow execution limits
```

### Branch Strategy for Solo Development
```
Use these prefixes for clear LLM communication:
- feature/yaml-*: YAML configuration features
- feature/dask-*: DASK integration improvements  
- feature/integration-*: Package integration work
- feature/llm-*: LLM coordination features
```