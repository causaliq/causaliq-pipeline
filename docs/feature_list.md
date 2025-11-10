# CausalIQ Pipeline - Feature List (Three-Month Plan)

## Core Features by Implementation Phase

### Phase 1 Features (Month 1: Foundation)

#### YAML Configuration System
- **Basic workflow loading** - Parse and validate YAML workflow definitions
- **Schema validation** - Comprehensive validation with clear error messages
- **Configuration inheritance** - Create workflows based on templates with overrides
- **Dry-run capability** - Preview execution plan without running workflow
- **Parameter substitution** - Support variables and references in YAML

#### Series Concept Implementation
- **Series definition** - Core organizing principle for grouped experiments
- **Experiment expansion** - Convert series config into individual experiment tasks
- **Dataset/parameter combinations** - Automatic generation across sample sizes, algorithms, hyperparameters
- **Series comparison support** - Framework for analyzing results across series using metrics such as SHD, BIC, F1 etc

#### Basic DASK Integration
- **Local cluster management** - Setup and manage local DASK clusters
- **Simple task graphs** - Convert basic workflows to DASK execution graphs
- **Progress monitoring** - Track workflow execution with basic progress indicators
- **Resource estimation** - Estimate compute requirements for workflow planning

#### Logging and Monitoring
- **Configurable logging** - Multiple log levels to avoid information overload
- **Progress indicators** - Real-time updates for long-running experiments
- **Error capture** - Detailed error reporting with context preservation
- **Execution metadata** - Track timing, resource usage, and workflow history

### Phase 2 Features (Month 2: Research Integration)

#### External Package Integration
- **R bnlearn plugin** - Execute R bnlearn algorithms from Python workflows
- **Java Tetrad plugin** - Integration with Java-based Tetrad algorithms  
- **Package discovery** - Automatic detection of available external packages
- **Dependency validation** - Check required packages before workflow execution
- **Error handling** - Robust handling of external package failures

#### Dataset Management
- **Dataset caching** - Local storage and reuse of downloaded datasets
- **Randomization capabilities** - Subsampling, variable reordering, noise injection
- **Dataset metadata** - Track dataset versions and transformations

#### LLM Integration Hooks
- **Model averaging coordination** - Framework for LLM-guided model averaging
- **Hypothesis generation** - Integration points for LLM hypothesis generation
- **Result interpretation** - LLM analysis of experimental results
- **Research workflow support** - Specific features for May 2026 research paper

#### Advanced Series Management
- **Cross-series analysis** - Compare results across different algorithmic approaches
- **Statistical testing** - Built-in statistical significance testing
- **Result aggregation** - Combine and summarize results across experiments
- **Experiment grouping** - Flexible organization of related experiments

### Phase 3 Features (Month 3: Production)

#### Workflow Management
- **Pause/resume functionality** - Interrupt and restart long-running workflows
- **Checkpoint system** - Save intermediate state for recovery
- **Workflow queuing** - Manage multiple concurrent workflows
- **Priority management** - Control execution order and resource allocation

#### Resource Management
- **Runtime limits** - Configurable time limits per experiment/workflow
- **Memory monitoring** - Track and limit memory usage
- **Resource scaling** - Dynamic allocation based on workflow requirements
- **Job prioritization** - Intelligent scheduling of experiments

#### Robust Error Handling
- **Fault tolerance** - Continue execution when individual experiments fail
- **Error recovery** - Automatic retry with exponential backoff
- **Graceful degradation** - Provide partial results when possible
- **Detailed diagnostics** - Comprehensive error reporting and debugging info

#### Results Management
- **Standardized formats** - Replace pickle files with human-readable formats
- **Result export** - Multiple output formats (CSV, JSON, HDF5)
- **Version tracking** - Track algorithm versions and parameter changes
- **Reproducibility support** - Complete metadata for result reproduction

## Post Three-Month Features (Outlook)

### Q2 2026: Research Phase Features
- **Advanced LLM integration** - Full implementation for intelligent model averaging
- **Interactive workflows** - Support for researcher-guided experiment refinement
- **Domain knowledge integration** - Incorporate expert knowledge into workflows
- **Publication support** - Generate reproducible research outputs

### Zenodo Integration
- **Zenodo download** - Automatic dataset download using zenodo-sync
- **Zenodo upload** - upload of results and workflow configurations

### Q3-Q4 2026: Migration Phase Features
- **Legacy workflow import** - Convert existing workflows to new format
- **Result validation** - Ensure exact replication of published results
- **Batch migration tools** - Utilities for systematic workflow conversion
- **Dual-system operation** - Run old and new systems in parallel
- **Statistical Significance** - capabilities added

### Q3-Q4 2026: Additional capabilities
- **inference and prediction** capabilities added

### Beyond 2026: Advanced Features
- **Multi-machine execution** - Distributed workflows across clusters
- **GPU integration** - Support for GPU-accelerated algorithms
- **Containerization** - Docker/Apptainer workflow packaging
- **Web GUI** - Graphical interface for workflow design and monitoring
- **Cloud deployment** - Support for cloud-based execution

## Success Criteria by Phase

### Phase 1 Success Metrics
- [ ] Execute YAML-defined series workflows locally
- [ ] Validate configuration files with clear error messages  
- [ ] Generate and preview execution plans via dry-run
- [ ] Basic progress monitoring for multi-experiment workflows
- [ ] Configuration inheritance working for workflow templates

### Phase 2 Success Metrics
- [ ] R bnlearn and Python algorithms running in same workflow
- [ ] Automatic dataset download and caching from Zenodo
- [ ] Series-based experiments with randomization strategies
- [ ] LLM integration framework ready for research use
- [ ] Cross-series comparison and analysis capabilities

### Phase 3 Success Metrics
- [ ] Pause and resume complex multi-hour workflows
- [ ] Resource limits preventing runaway experiments
- [ ] Robust error handling with partial result preservation
- [ ] Production-ready standardized result formats
- [ ] Foundation complete for existing workflow migration

This feature list provides a concrete roadmap for the three-month implementation while maintaining sight of longer-term goals.