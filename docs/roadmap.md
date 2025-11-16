# CausalIQ Workflow - Development Roadmap & Progress

**Single source of truth for all development planning and progress tracking**

Last updated: 2025-11-13

## Current Status: Phase 1-2 Transition - Action Framework + Workflow Engine [90% COMPLETE]

### 🎯 Major Achievement: Complete Action Framework + WorkflowExecutor Implementation

**Key Breakthrough**: We've successfully implemented both a robust action framework AND the core workflow execution engine. The framework provides type-safe action composition, comprehensive error handling, proven patterns for workflow orchestration, and now includes complete YAML workflow parsing with matrix expansion capabilities.

**Latest Achievement**: WorkflowExecutor class with 99-line implementation featuring YAML workflow parsing, cartesian product matrix expansion, dynamic path construction, and comprehensive schema validation - all with 100% test coverage (65 tests total).

**Implementation Highlights**:
- ✅ **Action framework foundation** - Abstract base classes with type-safe input/output specifications
- ✅ **GraphML format adoption** - Design decision for causal graph representation (DAGs, PDAGs, CPDAGs, MAGs, PAGs)
- ✅ **Matrix variable architecture** - Schema support for parameterized experiments
- ✅ **GitHub Actions-inspired syntax** - Familiar workflow patterns with schema validation

## Phase 1 Features (Month 1): Action Framework Foundation ✅ 100% Complete

### ✅ Foundation Infrastructure [COMPLETED] 
- [x] **Testing framework** - Comprehensive pytest setup covering unit, functional, integration (47/47 tests passing)
- [x] **CI/CD workflow** - GitHub Actions workflow with linting, formatting, type checking
- [x] **Code quality** - Black, isort, flake8, MyPy integration with 100% compliance
- [x] **Documentation structure** - MkDocs integration for API documentation
- [x] **Development environment** - Complete workspace setup with proper tooling
- [x] **Configuration foundation** - JSON Schema-based workflow validation established

### ✅ Action Framework [COMPLETED]
- [x] **Action base classes** - Abstract Action class with type-safe input/output specifications
- [x] **Error handling** - ActionExecutionError and ActionValidationError with comprehensive context
- [x] **Input/output specification** - ActionInput dataclass for type hints and validation
- [x] **Reference implementation** - DummyStructureLearnerAction demonstrating framework patterns
- [x] **GraphML format decision** - Adopted GraphML as standard for causal graph representation
- [x] **Matrix variable support** - Actions receive dataset, algorithm, and parameter inputs

### ✅ Workflow Schema Integration [COMPLETED]
- [x] **GitHub Actions-inspired syntax** - Familiar workflow patterns adapted for causal discovery
- [x] **Matrix strategy support** - Parameterized experiments with matrix variable expansion
- [x] **Path construction fields** - data_root, output_root, id fields for organizing experiment outputs  
- [x] **Action parameters** - with blocks for passing parameters to actions
- [x] **Schema validation** - JSON Schema validation with comprehensive error reporting

## Phase 2 Features (Current): Workflow Execution Engine [60% Complete]

### ✅ CI-Style Workflow Engine [COMPLETED]
- [x] **WorkflowExecutor class** - Complete 99-line implementation with comprehensive testing (65 total tests, 100% coverage)
- [x] **Workflow parser** - Parse GitHub Actions-style YAML workflows with schema validation
- [x] **Matrix expansion** - Convert matrix variables into individual experiment jobs using cartesian product
- [x] **Path construction** - Dynamic file path generation from matrix variables with flexible templating
- [x] **Schema validation** - JSON Schema validation with corrected $schema/$id fields and required id/description
- [x] **Error handling** - Comprehensive validation and parsing error management

### 🔄 Research Reproducibility Platform [SIMPLIFIED ARCHITECTURE - 5 Commits to Working Workflow]

**Architectural Focus**: Start with simple sequential step execution and matrix expansion. Add complexity only when proven necessary.

**Commit 1: Template Variable Validation** ✅ **COMPLETED**
- [x] **Template extraction** - Parse `{{variable}}` patterns from action parameters
- [x] **Context validation** - Verify template variables exist in matrix + workflow properties
- [x] **Error reporting** - Clear errors for unknown/malformed template variables
- [x] **Comprehensive tests** - Cover valid, invalid, and malformed template scenarios

**Commit 2: Intelligent Action Framework & Conservative Execution**
- [ ] **Package-level actions** - Actions like `causaliq-discovery` with algorithm parameters (no required versioning)
- [ ] **Conservative execution** - Actions skip work if outputs exist, enabling safe workflow restarts
- [ ] **Mode-based operation** - `--mode=dry-run|run|compare` for validation, execution, and functional testing
- [ ] **Smart action capabilities** - Actions optimize internally (dataset loading, caching) transparently to users
- [ ] **Action-level validation** - Actions validate their own inputs (integrated with dry-run mode)
- [ ] **Standardized output format** - Fixed filenames by type (graph.xml, metadata.json, trace.csv)

**Commit 3: CLI & Workflow Composition**
- [ ] **CLI implementation** - `cwork` command with parameter injection: `cwork workflow.yml --network=asia`
- [ ] **Workflow calling capability** - `cwork` commands in workflow steps for composition
- [ ] **Template parameter flow** - CLI and caller parameters available as `{{parameter}}` in workflows
- [ ] **Flexible parameter model** - No rigid workflow input schemas, actions decide what they need

**Commit 4: Action Registry & Step Execution Engine**
- [ ] **ActionRegistry class** - Centralized registry for action discovery and instantiation  
- [ ] **Step executor** - Execute `uses:` action steps via ActionRegistry
- [ ] **Shell command support** - Handle `run:` command execution and `cwork` workflow calling
- [ ] **Parameter mapping** - Map workflow `with:` blocks to action inputs with CLI parameter injection

**Commit 5: Production CLI & Real Actions**
- [ ] **Enhanced CLI** - Full `cwork` implementation with mode support: `cwork workflow.yml --network=asia --mode=run`
- [ ] **Real algorithm actions** - PC, GES, FCI structure learning implementations via causaliq-discovery
- [ ] **CausalIQ package integration** - causaliq-discovery, causaliq-analysis, causaliq-knowledge, causaliq-papers
- [ ] **Hierarchical output organization** - Standardized folder structures for experiment results

**Milestone Achievement**: After these 5 commits, CausalIQ Workflow will support:
- ✅ **Sequential step execution** with matrix expansion
- ✅ **Intelligent action optimization** with dry-run and caching
- ✅ **Workflow composition** via CLI parameter passing and shell commands
- ✅ **Research reproducibility platform** foundation for causaliq-papers integration

### 🔮 Future Enhancements [When Proven Necessary]

**Parallel Jobs Support**: Add `jobs:` syntax and parallel execution when performance demands require it
**DASK Integration**: Step-level parallelization for computationally intensive actions  
**Formal Parameter Schemas**: Optional workflow input definitions for enhanced validation when workflows become complex
- ✅ **DASK-powered task parallelization** within steps
- ✅ **Workflow composition** via calling with parameters
- ✅ **Intelligent action optimization** with dry-run and caching
- ✅ **Research reproducibility platform** foundation for causaliq-papers integration
- [ ] **Data file handling** - Read actual CSV datasets and produce results
- [ ] **Algorithm parameters** - Support real algorithm configuration options

**Milestone Achievement**: After these 8 commits, CausalIQ Workflow will support:
- ✅ **Parallel job execution** with dependency management
- ✅ **DASK-powered task parallelization** within steps
- ✅ **Workflow composition** via calling with parameters
- ✅ **Intelligent action optimization** with dry-run and caching
- ✅ **Research reproducibility platform** foundation for causaliq-papers integration

### 🔮 Research Reproducibility Ecosystem [FUTURE - Integration with causaliq-papers]

**Vision**: CausalIQ Workflow serves as the execution engine for a comprehensive research reproducibility platform.

**causaliq-papers Integration Architecture**:
```bash
# High-level research reproducibility workflow
causaliq-papers replicate peters2023causal --target=figure3

# causaliq-papers processes paper dependencies and generates:
├── workflow-dependencies.yml    # Analyzes what's needed for figure3
├── optimized-reproduction.yml   # Generates minimal workflow-of-workflows
└── execution-plan.json         # Dependency graph for execution

# Then calls causaliq-workflow to execute:
causaliq-workflow run optimized-reproduction.yml --target=figure3
```

**Workflow-of-Workflows Pattern**:
- **Paper reproduction** = Top-level workflow calling component workflows
- **Dependency resolution** = causaliq-papers analyzes workflow graph to minimize execution
- **Asset targeting** = Generate only requested paper assets (tables, figures, results)
- **Intelligence integration** = Actions optimize across the entire workflow graph

### ⏸️ Algorithm Integration [FUTURE - After Working Workflow]
- [ ] **Advanced algorithms** - Additional causal discovery algorithms beyond PC/GES
- [ ] **Package plugins** - bnlearn (R), Tetrad (Java), causal-learn (Python) integration
- [ ] **Cross-language bridges** - rpy2, py4j integration for R/Java algorithm access
- [ ] **Algorithm benchmarking** - Systematic comparison across algorithm implementations

## Success Metrics - Phase 1 ✅ + Phase 2 Partial ✅

- ✅ **Framework Foundation**: Action framework with type-safe interfaces implemented
- ✅ **Schema Architecture**: GitHub Actions-inspired workflow syntax with matrix support  
- ✅ **Reference Implementation**: DummyStructureLearnerAction proving framework viability
- ✅ **Format Decision**: GraphML adopted as standard for causal graph representation
- ✅ **Workflow Parsing**: Complete WorkflowExecutor with YAML parsing and matrix expansion
- ✅ **Path Construction**: Dynamic file path generation from matrix variables
- ✅ **Schema Validation**: Corrected JSON Schema with proper $id field and field requirements
- ✅ **Test Coverage**: 100% coverage maintained across 65 comprehensive tests

## Next Milestone: Functional Causal Discovery Workflow

**Target**: Complete working workflow capable of executing real causal discovery experiments
**Success Criteria**: 
- Execute complete workflows from command line
- Support real structure learning algorithms (PC, GES)
- Handle matrix expansion with parallel step execution  
- Generate organized experimental outputs with GraphML graphs
- Maintain 100% test coverage and CI compliance

**Timeline**: 4 focused commits transitioning from framework to working research tool
  - ✅ Required/optional section validation per pattern
  - ✅ Hierarchical field validation with detailed error reporting
  - ✅ Flexible validation schemas defined in external YAML
- [x] **Flexible workflow patterns** - 5 patterns supporting diverse research needs
  - ✅ Series pattern for comparative research (algorithm comparison across datasets/parameters)
  - ✅ Task pattern for sequential operations (preprocessing → algorithm → analysis)  
  - ✅ Mixed pattern combining multiple approaches
  - ✅ Workflow pattern for DAG-based workflows with dependencies
  - ✅ Longitudinal_research pattern for temporal causal discovery studies
- [ ] **Configuration inheritance** - Create workflows based on templates with overrides
### ✅ CI-Style Workflow Engine [COMPLETED]
- [x] **Workflow parser** - Parse GitHub Actions-style YAML workflows
- [x] **Matrix expansion** - Convert matrix variables into individual experiment jobs  
- [x] **Path construction** - Dynamic file path generation from matrix variables
- [x] **Schema validation** - JSON Schema validation with required id/description fields
- [x] **WorkflowExecutor class** - Complete 99-line implementation with comprehensive testing
- [ ] **Step execution** - Execute workflow steps with action-based architecture
- [ ] **Environment management** - Handle workflow environment variables and context
- [ ] **Conditional execution** - Support `if:` conditions in workflow steps
- [ ] **Artifact handling** - Manage inputs/outputs between workflow steps

### ⏸️ DASK Task Graph Integration [PENDING]
- [ ] **Matrix job expansion** - Convert matrix configs into DASK task graphs
- [ ] **Dependency management** - Handle job dependencies with DASK
- [ ] **Local cluster management** - Setup and manage local DASK clusters
- [ ] **Progress monitoring** - Track workflow execution with real-time updates
- [ ] **Resource estimation** - Estimate compute requirements for planning

### ⏸️ Configuration Migration [PENDING]
- [ ] **CI workflow validation** - Ensure CI workflows validate correctly
- [ ] **Documentation update** - Update all docs to reflect CI workflow approach

## Phase 2 Features (Month 2): Research Integration [NOT STARTED]

### ⏸️ Algorithm Package Integration
- [ ] **R bnlearn integration** - Execute R bnlearn algorithms via rpy2
  - Matrix-driven algorithm selection: `algorithm: ["pc", "iamb", "gs"]`
- [ ] **Java Tetrad integration** - Integration with Java-based Tetrad via py4j
  - Cross-language workflow steps with data serialization
- [ ] **Python causal-learn** - Direct integration with Python algorithms
  - Native Python execution within workflow steps
- [ ] **Package discovery** - Automatic detection of available packages
- [ ] **Dependency validation** - Check required packages before workflow execution

### ⏸️ Dataset Management with CI Patterns
- [ ] **Zenodo integration** - Dataset download as workflow action
  - `uses: zenodo-download@v1` action pattern
- [ ] **Dataset caching** - Local storage and reuse with cache actions
- [ ] **Matrix dataset expansion** - Multiple datasets in workflow matrix
  - `matrix: {dataset: ["asia", "sachs"], sample_size: [100, 1000]}`
- [ ] **Dataset transformations** - Preprocessing steps as workflow actions

### ⏸️ Advanced Matrix Workflows
- [ ] **Cross-product expansion** - Full matrix combinations with intelligent batching
- [ ] **Conditional matrices** - Include/exclude matrix combinations based on conditions
- [ ] **Matrix job dependencies** - Sequential and parallel matrix job orchestration
- [ ] **Result aggregation** - Collect and combine results across matrix jobs

### ⏸️ LLM Integration as Actions
- [ ] **Model averaging action** - LLM-guided model averaging as reusable action
- [ ] **Hypothesis generation** - LLM analysis steps in workflow
- [ ] **Result interpretation** - LLM post-processing actions
- [ ] **Research workflow templates** - Pre-built workflows for common research patterns

## Phase 3 Features (Month 3): Production CI Features [NOT STARTED]

### ⏸️ Advanced Workflow Management
- [ ] **Workflow queuing** - Manage multiple concurrent workflows like CI runners
- [ ] **Pause/resume** - Interrupt and restart workflows with state preservation
- [ ] **Workflow artifacts** - Persistent storage and retrieval of workflow outputs
- [ ] **Workflow caching** - Cache intermediate results for faster re-runs
- [ ] **Branch/PR workflows** - Different workflows for different experiment branches

### ⏸️ Enterprise CI Features
- [ ] **Secrets management** - Secure handling of API keys and credentials
- [ ] **Environment isolation** - Containerized execution environments
- [ ] **Resource limits** - CPU, memory, and time limits per workflow/job
- [ ] **Approval workflows** - Human approval steps for expensive experiments
- [ ] **Scheduled workflows** - Cron-style scheduled execution

### ⏸️ Monitoring and Observability  
- [ ] **Workflow status dashboard** - Real-time workflow execution monitoring
- [ ] **Job logs and traces** - Detailed logging with searchable history
- [ ] **Performance metrics** - Resource usage, timing, and efficiency tracking
- [ ] **Alert integration** - Notifications for workflow success/failure
- [ ] **Audit trail** - Complete execution history for reproducibility

### ⏸️ Results and Artifacts
- [ ] **Standardized outputs** - Replace pickle files with structured formats
- [ ] **Version tracking** - Track algorithm versions and parameter changes
- [ ] **Result comparison** - Compare outputs across workflow runs
- [ ] **Export capabilities** - Multiple output formats (CSV, JSON, HDF5)
- [ ] **Reproducibility metadata** - Complete metadata for result reproduction

## Success Criteria by Phase

### Phase 1 Success Metrics  
- [ ] Execute GitHub Actions-style YAML workflows locally
- [ ] Matrix expansion generates individual causal discovery jobs
- [ ] Package-level algorithm integration (bnlearn, Tetrad, causal-learn)
- [ ] DASK task graph execution with progress monitoring
- [ ] Jinja2 template processing for workflow variables

### Phase 2 Success Metrics
- [ ] Multi-language workflows (R, Java, Python) in single configuration
- [ ] Automatic dataset download and matrix expansion across datasets
- [ ] LLM integration actions for model averaging and analysis
- [ ] Advanced matrix workflows with conditional execution
- [ ] Research workflow templates for common causal discovery patterns

### Phase 3 Success Metrics  
- [ ] Production-grade workflow queue management
- [ ] Enterprise features: secrets, isolation, limits, approvals
- [ ] Comprehensive monitoring dashboard with real-time status
- [ ] Standardized result formats with complete reproducibility metadata
- [ ] Foundation ready for large-scale research deployment

## Post Three-Month Features (Research Phase)

### Q2 2026: Advanced Research Features
- **Workflow marketplace** - Sharing and discovering research workflow templates
- **Interactive notebooks** - Jupyter integration with workflow execution
- **Publication workflows** - Generate reproducible research outputs automatically
- **Domain knowledge integration** - Expert knowledge as workflow conditions

### Q3-Q4 2026: Migration and Scale
- **Multi-machine execution** - Distributed workflows across compute clusters
- **Cloud provider integration** - AWS, GCP, Azure workflow runners
- **GPU acceleration** - Support for GPU-accelerated algorithms
- **Web interface** - Browser-based workflow designer and monitor

### Beyond 2026: Advanced Capabilities
- **Workflow orchestration** - Complex multi-stage research workflows
- **Real-time collaboration** - Multiple researchers on shared workflows
- **AI-assisted optimization** - Automated hyperparameter and workflow tuning
- **Integration ecosystem** - Plugins for major research tools and platforms

This roadmap leverages the familiar GitHub Actions paradigm while building a powerful platform specifically designed for causal discovery research workflows.