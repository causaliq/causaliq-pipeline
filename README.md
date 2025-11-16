# causaliq-workflow

[![Python Support](https://img.shields.io/pypi/pyversions/zenodo-sync.svg)](https://pypi.org/project/zenodo-sync/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**GitHub Actions-inspired workflow orchestration for causal discovery experiments** within the [CausalIQ ecosystem](https://github.com/causaliq/causaliq). Execute causal discovery workflows using familiar CI/CD patterns with conservative execution and comprehensive action framework.

## Current Implementation (v0.1.0)

✅ **Action Framework Foundation Complete** - Robust workflow orchestration with 100% test coverage

```yaml
description: "Causal Discovery Experiment"
id: "experiment-001"

matrix:
  network: ["asia", "cancer"]
  algorithm: ["pc", "ges"]
  sample_size: ["100", "1K"]

steps:
  - name: "Structure Learning"
    uses: "causaliq-discovery"
    with:
      algorithm: "{{algorithm}}"
      sample_size: "{{sample_size}}"
      dataset: "/data/{{network}}"
      output: "/results/{{id}}/{{algorithm}}/{{network}}/{{sample_size}}"
```

**Execute with modes:**
```bash
cwork experiment.yml --mode=dry-run    # Validate and preview (default)
cwork experiment.yml --mode=run        # Execute (skip if outputs exist)
cwork experiment.yml --mode=compare    # Re-execute and compare outputs
```

Note that **cwork** is a short synonym for **causaliq-workflow** which can also be used.

## Implementation Status

� **Phase 1: Action Framework Foundation** - ✅ 75% Complete (47/47 tests passing)

**Completed Features**:
- ✅ **Action Framework**: Type-safe action base classes with comprehensive error handling
- ✅ **Schema Validation**: GitHub Actions-inspired workflow syntax with matrix support
- ✅ **Test Coverage**: 100% coverage across unit, functional, and integration tests
- ✅ **Reference Implementation**: DummyStructureLearnerAction demonstrating framework

📋 **Complete progress tracking**: [docs/roadmap.md](docs/roadmap.md)

## Key Features

- **🎯 GitHub Actions Syntax**: Familiar workflow patterns adapted for causal discovery
- **📊 Matrix Variables**: Parameterized experiments with hierarchical output organization
- **🔧 CausalIQ Actions**: Reusable workflow actions from causaliq-discovery, causaliq-analysis packages
- **⚡ Conservative Execution**: Skip work if outputs exist, enabling safe restarts and efficient re-runs
- **🛡️ Mode-Based Operation**: dry-run (validate), run (execute), compare (functional testing)
- **🗂️ Standardized Output**: Fixed filenames by type (graph.xml, metadata.json, trace.csv)
- **🧪 Comprehensive Testing**: Unit, functional, and integration tests with tracked test data

**See detailed architecture**: [docs/technical_architecture.md](docs/technical_architecture.md)

## Quick Start

### Prerequisites
- Python 3.9-3.12
- Git
- R with bnlearn (optional, for external integration)

### Installation
```bash
git clone https://github.com/causaliq/causaliq-workflow.git
cd causaliq-workflow

# Set up development environment
scripts/setup-env.ps1 -Install
scripts/activate.ps1 311
```

**Example workflows**: [docs/example_workflows.md](docs/example_workflows.md)

## Documentation

- **[📋 Development Roadmap](docs/roadmap.md)** - Complete roadmap and delivery specifications
- **[🏗️ Technical Architecture](docs/technical_architecture.md)** - CI workflow engine design and core components
- **[⚙️ CI Workflow Implementation](docs/design/ci_workflow_implementation.md)** - Strategic design decisions and implementation approach
- **[📊 Matrix Strategy Design](docs/design/matrix_expansion_design.md)** - GitHub Actions matrix implementation details
- **[🔧 Action Architecture](docs/design/action_architecture_design.md)** - Versioned action component system
- **[🔌 Algorithm Registry](docs/design/algorithm_registry_design.md)** - Package-level plugin architecture

## CausalIQ Ecosystem Integration

Coordinates with:
- **causaliq-discovery**: Core algorithms (integrated as package plugins)
- **causaliq-knowledge**: Provides knowledge, including from LLMs, via action-based architecture
- **causaliq-analysis**: Statistical analysis actions and post-processing  
- **causaliq-papers**: Configuration and result storage for to enable reproducibility of CausalIQ papers

## Research Context

Supporting research for May 2026 paper on LLM integration for intelligent model averaging. The CI workflow architecture enables sophisticated experimental designs while maintaining familiar syntax for the research community.

**Migration target**: Existing workflows from monolithic discovery repo by end 2026.

## License

MIT License - see [LICENSE](LICENSE) file.

---

**Supported Python Versions**: 3.9, 3.10, 3.11, 3.12  
**Default Python Version**: 3.11
