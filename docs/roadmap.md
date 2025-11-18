# CausalIQ Workflow - Development Roadmap & Progress

**Single source of truth for all development planning and progress tracking**

Last updated: 2025-11-18

## Current Status: Phase 1-2 Complete - Action Framework + Workflow Engine [99% COMPLETE]

### 🎯 Major Achievement: Complete Action Registry System + Dynamic Plugin Discovery

**Key Breakthrough**: We've successfully implemented the complete action registry system with automatic discovery, enabling a true plugin ecosystem for causal discovery workflows. The registry provides zero-configuration action discovery, automatic registration, and seamless integration with the workflow execution engine.

**Latest Achievement**: Complete ActionRegistry implementation with auto-discovery via import-time introspection, comprehensive test action package demonstrating the plugin pattern, and full integration with WorkflowExecutor for end-to-end action execution. The system now supports dynamic action loading from external packages without circular dependencies.

**Action Registry Highlights**:
- ✅ **Zero-configuration discovery** - Actions automatically discovered via import-time introspection using 'CausalIQAction' convention
- ✅ **Plugin architecture** - Complete test action package demonstrating external action development patterns
- ✅ **Seamless integration** - WorkflowExecutor now executes actions via ActionRegistry with full parameter mapping
- ✅ **Comprehensive validation** - Registry validates action availability and provides detailed error reporting
- ✅ **Production-ready pattern** - External packages export 'CausalIQAction' class and become immediately available in workflows
- ✅ **Complete documentation** - Registry API documentation with usage examples and architecture notes
- ✅ **100% test coverage maintained** - Registry and integration fully tested with comprehensive edge case coverage

**Implementation Highlights**:
- ✅ **Action framework foundation** - Abstract base classes with type-safe input/output specifications
- ✅ **GraphML format adoption** - Design decision for causal graph representation (DAGs, PDAGs, CPDAGs, MAGs, PAGs)
- ✅ **Matrix variable architecture** - Schema support for parameterized experiments
- ✅ **GitHub Actions-inspired syntax** - Familiar workflow patterns with schema validation
- ✅ **WorkflowExecutor class** - 99-line implementation featuring YAML workflow parsing, matrix expansion, and comprehensive validation

## Phase 1 Features (Month 1): Action Framework Foundation ✅ 100% Complete

### ✅ Foundation Infrastructure [COMPLETED] 
- [x] **Testing framework** - Comprehensive pytest setup covering unit, functional, integration (112/112 tests passing)
- [x] **CI/CD workflow** - GitHub Actions workflow with linting, formatting, type checking
- [x] **Code quality** - Black, isort, flake8, MyPy integration with 100% compliance
- [x] **Documentation structure** - MkDocs integration with restructured API documentation
- [x] **API documentation** - Comprehensive 6-page API reference with Google-style docstrings
- [x] **Development environment** - Complete workspace setup with proper tooling
- [x] **Configuration foundation** - JSON Schema-based workflow validation established
- [x] **Test policy compliance** - Function-based test structure with single-line comments

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

## Phase 2 Features (Current): Workflow Execution Engine [95% Complete]

### ✅ CI-Style Workflow Engine [COMPLETED]
- [x] **WorkflowExecutor class** - Complete 99-line implementation with comprehensive testing (112 total tests, 100% coverage)
- [x] **Workflow parser** - Parse GitHub Actions-style YAML workflows with schema validation
- [x] **Matrix expansion** - Convert matrix variables into individual experiment jobs using cartesian product
- [x] **Path construction** - Dynamic file path generation from matrix variables with flexible templating
- [x] **Schema validation** - JSON Schema validation with corrected $schema/$id fields and required id/description
- [x] **Error handling** - Comprehensive validation and parsing error management
- [x] **Template variable system** - Full template validation with context checking and error reporting

### ✅ Documentation Infrastructure [COMPLETED]
- [x] **API restructure** - Separated API documentation into focused, navigable pages
- [x] **Google-style docstrings** - Complete class variable documentation for comprehensive API coverage  
- [x] **Cross-linking** - Proper navigation between API sections with back/forward links
- [x] **Usage examples** - Comprehensive examples covering basic to advanced usage patterns
- [x] **MkDocs integration** - Updated navigation structure with proper page organization
- [x] **CI integration** - Documentation builds without warnings or broken links

### 🔄 Research Reproducibility Platform [STREAMLINED 3-COMMIT APPROACH]

**Architectural Focus**: Optimized path to working CLI with external actions. Start with dynamic action discovery and build incrementally.

### 🔄 Research Reproducibility Platform [STREAMLINED 3-COMMIT APPROACH]

**Architectural Focus**: Optimized path to working CLI with external actions. Start with dynamic action discovery and build incrementally.

**Commit 1: Template Variable Validation** ✅ **COMPLETED**
- [x] **Template extraction** - Parse `{{variable}}` patterns from action parameters
- [x] **Context validation** - Verify template variables exist in matrix + workflow properties
- [x] **Error reporting** - Clear errors for unknown/malformed template variables
- [x] **Comprehensive tests** - Cover valid, invalid, and malformed template scenarios

**Commit 2: Documentation & Test Infrastructure** ✅ **COMPLETED**
- [x] **API documentation restructure** - Separated into focused pages (Actions, Registry, Workflow, Schema, CLI, Examples)
- [x] **Google-style docstrings** - Complete class variable documentation for API generation
- [x] **Test policy compliance** - Converted major test files to function-based structure with single-line comments
- [x] **100% test coverage** - Maintained comprehensive coverage across 112 tests
- [x] **MkDocs integration** - Updated navigation and cross-linking structure
- [x] **Documentation quality** - Eliminated broken links and warnings

**Commit 3: Action Registry & Step Execution Engine** ✅ **COMPLETED**
- [x] **ActionRegistry class** - Centralized registry for dynamic action discovery via import-time introspection
- [x] **Dynamic discovery** - Load actions from imported packages using convention-over-configuration
- [x] **Step executor** - Complete integration with WorkflowExecutor for `uses:` action step execution
- [x] **Action execution** - Full mapping of workflow `with:` blocks to action inputs with validation
- [x] **Error handling** - Comprehensive action discovery and execution error management
- [x] **Plugin architecture** - Zero-configuration plugin system with test action package demonstrating pattern

**Commit 4: CLI Implementation & Mode Support** 🔑 **NEXT**
- [ ] **`causaliq-workflow` command** - Complete CLI with workflow file execution using ActionRegistry
- [ ] **Mode-based operation** - `--mode=dry-run|run|compare` for validation, execution, and testing
- [ ] **Parameter injection** - CLI parameters available as template variables via WorkflowExecutor
- [ ] **CLI error handling** - User-friendly error reporting for workflow and action failures
- [ ] **Workflow validation** - Pre-execution validation with clear error messages via ActionRegistry

**Commit 5: External Package Integration & Demo**
- [ ] **causaliq-discovery package** - Simple structure learning action (PC algorithm)
- [ ] **Entry point registration** - Dynamic discovery working with external package
- [ ] **End-to-end workflow** - Complete example: CLI → ActionRegistry → External action → Results
- [ ] **Real algorithm execution** - PC structure learning with actual data processing
- [ ] **Output standardization** - GraphML files and standardized result formats

**Milestone Achievement**: After these 5 commits, CausalIQ Workflow will support:
- ✅ **Complete documentation infrastructure** - Comprehensive API reference with proper navigation
- ✅ **Template variable validation** - Full context checking and error reporting
- ✅ **Test infrastructure compliance** - Function-based test structure with 100% coverage
- ✅ **Dynamic action discovery** - Load actions from external packages via import-time introspection
- [ ] **Complete CLI interface** - Full `causaliq-workflow` command with mode support and parameter injection
- [ ] **External action execution** - Real structure learning via causaliq-discovery package
- [ ] **Conservative execution** - Skip work if outputs exist, enabling safe workflow restarts  
- [ ] **Research reproducibility foundation** - Ready for causaliq-papers integration

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

## Success Metrics - Phase 1 ✅ + Phase 2 ✅

- ✅ **Framework Foundation**: Action framework with type-safe interfaces implemented
- ✅ **Schema Architecture**: GitHub Actions-inspired workflow syntax with matrix support  
- ✅ **Reference Implementation**: DummyStructureLearnerAction proving framework viability
- ✅ **Format Decision**: GraphML adopted as standard for causal graph representation
- ✅ **Workflow Parsing**: Complete WorkflowExecutor with YAML parsing and matrix expansion
- ✅ **Path Construction**: Dynamic file path generation from matrix variables
- ✅ **Schema Validation**: Corrected JSON Schema with proper $id field and field requirements
- ✅ **Test Coverage**: 100% coverage maintained across 112 comprehensive tests
- ✅ **Documentation Infrastructure**: Complete API reference with structured navigation
- ✅ **Template System**: Full template variable validation and context checking
- ✅ **Code Quality**: Policy-compliant test structure with function-based organization
- ✅ **Action Registry**: Complete plugin architecture with auto-discovery and validation
- ✅ **Plugin System**: Zero-configuration action packages with production-ready patterns

## Next Milestone: Functional Causal Discovery Workflow

**Target**: Complete working workflow capable of executing real causal discovery experiments
**Success Criteria**: 
- Execute complete workflows from command line
- Support real structure learning algorithms (PC, GES)
- Handle matrix expansion with parallel step execution  
- Generate organized experimental outputs with GraphML graphs
- Maintain 100% test coverage and CI compliance
- Comprehensive API documentation with proper navigation

**Timeline**: 2 focused commits remaining to transition from framework to working research tool
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