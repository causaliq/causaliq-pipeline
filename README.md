# causaliq-pipeline

[![Python Support](https://img.shields.io/pypi/pyversions/zenodo-sync.svg)](https://pypi.org/project/zenodo-sync/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Workflow orchestration for causal discovery experiments** within the [CausalIQ ecosystem](https://github.com/causaliq/causaliq). Coordinates causal discovery algorithms using DASK and YAML configuration with a focus on series-based experiment organization.

## Status

🚧 **Active Development** - Currently implementing core framework (Month 1 of 3-month plan). See [Development Roadmap](docs/development_roadmap.md) for detailed timeline.

## Quick Overview

causaliq-pipeline orchestrates causal discovery experiments using:
- **Series concept**: Organize experiments across datasets, algorithms, and parameters
- **YAML configuration**: Define workflows with inheritance and validation
- **DASK execution**: Parallel execution with resource management
- **External integration**: R (bnlearn), Java (Tetrad), and Python packages
- **LLM coordination**: Integration with causaliq-llm for model averaging

## Three-Month Implementation Plan

### Phase 1 (Month 1): Foundation ✅ Current Focus
- YAML workflow configuration with validation
- Series concept for experiment organization  
- Basic DASK integration and task execution
- Simple logging and progress monitoring

### Phase 2 (Month 2): Integration
- External package plugins (R bnlearn, Java Tetrad)
- Dataset download and randomization via zenodo-sync
- LLM integration hooks for research
- Series-based experiment execution

### Phase 3 (Month 3): Production
- Pause/resume workflow functionality
- Resource monitoring and limits
- Robust error handling and recovery
- Foundation for existing workflow migration

## Core Technologies

- **DASK**: Parallel and distributed computing
- **YAML**: Configuration with inheritance support
- **Python 3.9-3.12**: Following CausalIQ ecosystem standards
- **Plugin Architecture**: R, Java, and Python package integration

## The "Series" Concept

Central organizing principle for causal discovery experiments:
```yaml
series:
  pc_experiments:
    algorithm: "pc"
    datasets: ["alarm", "asia"]
    sample_sizes: [100, 500, 1000]
    randomizations: 10
    hyperparameters:
      alpha: [0.01, 0.05, 0.1]
```

## Quick Start

### Prerequisites
- Python 3.9-3.12
- Git
- R with bnlearn (optional, for external integration)

### Installation
```bash
git clone https://github.com/causaliq/causaliq-pipeline.git
cd causaliq-pipeline

# Set up development environment
scripts/setup-env.ps1 -Install
scripts/activate.ps1 311
```

### Basic Usage
```bash
# Validate workflow configuration
causaliq-pipeline validate example_workflow.yaml --dry-run

# Execute workflow (when implemented)
causaliq-pipeline run example_workflow.yaml

# Monitor progress
causaliq-pipeline status workflow-123
```

## Example Workflow

```yaml
# pc_ges_comparison.yaml
metadata:
  name: "pc_ges_comparison"
  description: "Compare PC and GES algorithms"

series:
  pc_series:
    algorithm: "pc"
    package: "causaliq-discovery"
    datasets: ["alarm", "asia"]
    sample_sizes: [500, 1000]
    randomizations: 5
    hyperparameters:
      alpha: 0.05
      
  ges_series:
    algorithm: "ges"
    package: "causaliq-discovery" 
    datasets: ["alarm", "asia"]
    sample_sizes: [500, 1000]
    randomizations: 5
    hyperparameters:
      score_type: "bic"

analysis:
  compare_series: ["pc_series", "ges_series"]
  metrics: ["shd", "precision", "recall"]
```

## Documentation

- **[Requirements](docs/feature_list.md)** - Features and three-month implementation plan
- **[Technical Architecture](docs/technical_architecture.md)** - Technical Architecture
- **[Example Workflows](docs/example_workflows.md)** - Series-based workflow examples
- **[LLM Communication Guide](docs/llm_communication_guide.md)** - Working with LLMs on this project

## Position in CausalIQ Ecosystem

Integrates with other CausalIQ packages:
- **causaliq-discovery**: Core algorithms (gradual migration from monolithic repo)
- **causaliq-llm**: LLM integration for model averaging and analysis
- **causaliq-analysis**: Statistical analysis and metrics
- **causaliq-experiments**: Configuration and result storage
- **External packages**: R (bnlearn), Java (Tetrad)

## Research Context

Supporting research for May 2026 paper on LLM integration for intelligent model averaging. Also preparing for migration of existing workflows from monolithic discovery repo by end 2026.


## License

MIT License - see [LICENSE](LICENSE) file.

---

**Supported Python Versions**: 3.9, 3.10, 3.11, 3.12  
**Default Python Version**: 3.11
