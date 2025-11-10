# CausalIQ Pipeline - Technical Architecture

## System Overview

The causaliq-pipeline serves as the orchestration layer within the [CausalIQ ecosystem](https://github.com/causaliq/causaliq), coordinating causal discovery experiments through YAML-configured workflows executed via DASK. This architecture is designed around the "series" concept - groups of experiments that systematically compare algorithms across datasets, sample sizes, and hyperparameters.

## Integration with CausalIQ Ecosystem

### Coordinated Packages
- **causaliq-discovery**: Core algorithms (PC, GES, FCI) - gradual migration from monolithic repo
- **causaliq-llm**: LLM integration for model averaging and analysis  
- **causaliq-analysis**: Statistical analysis and metrics computation
- **causaliq-experiments**: Configuration and result storage for reproducibility
- **External packages**: R (bnlearn), Java (Tetrad) via plugin architecture

### Shared Standards
Follows [CausalIQ development practices](https://github.com/causaliq/causaliq/blob/main/CONTRIBUTING.md):
- Python 3.9-3.12 support
- Standardized project structure and testing
- Open standards for configurations and results

## Phase-Based Architecture Implementation

### Phase 1 Components (Month 1: Foundation)

#### 1. YAML Configuration System (`causaliq_pipeline.config`)

```python
class ConfigurationManager:
    """Handles YAML workflow configuration with inheritance and validation."""
    
    def load_workflow(self, yaml_path: str) -> WorkflowConfig:
        """Parse and validate YAML workflow definitions."""
        
    def validate_schema(self, config: WorkflowConfig) -> ValidationResult:
        """Comprehensive validation with clear error messages."""
        
    def inherit_configuration(self, base_config: str, overrides: Dict) -> WorkflowConfig:
        """Create workflows based on templates with overrides."""
        
    def dry_run_preview(self, config: WorkflowConfig) -> ExecutionPlan:
        """Preview execution plan without running workflow."""
        
    def substitute_parameters(self, config: WorkflowConfig) -> WorkflowConfig:
        """Support variables and references in YAML."""
```

#### 2. Series Concept Implementation (`causaliq_pipeline.series`)

```python
class SeriesManager:
    """Core organizing principle - groups of experiments across datasets/parameters."""
    
    def create_series(self, name: str, config: SeriesConfig) -> Series:
        """Series definition with automatic expansion capability."""
        
    def expand_experiments(self, series: Series) -> List[Experiment]:
        """Convert series config into individual experiment tasks."""
        
    def generate_combinations(self, datasets: List[str], sample_sizes: List[int], 
                            hyperparameters: Dict) -> List[ExperimentConfig]:
        """Automatic generation across datasets/parameters combinations."""
        
    def setup_series_comparison(self, series_names: List[str]) -> ComparisonFramework:
        """Framework for analyzing results across series using metrics (SHD, BIC, F1)."""
```

#### 3. Basic DASK Integration (`causaliq_pipeline.execution`)

```python
class LocalClusterManager:
    """Setup and manage local DASK clusters."""
    
    def create_local_cluster(self, workers: int, memory_per_worker: str) -> Client:
        """Local cluster management with resource configuration."""
        
    def monitor_cluster_health(self) -> ClusterStatus:
        """Basic cluster monitoring and health checks."""

class SimpleTaskGraphBuilder:
    """Convert basic workflows to DASK execution graphs."""
    
    def build_experiment_graph(self, experiments: List[Experiment]) -> Dict[str, Any]:
        """Simple task graphs for individual experiments."""
        
    def estimate_resources(self, experiments: List[Experiment]) -> ResourceEstimate:
        """Estimate compute requirements for workflow planning."""
        
    def add_progress_tracking(self, graph: Dict[str, Any]) -> Dict[str, Any]:
        """Add progress monitoring to task graph."""
```

#### 4. Logging and Monitoring (`causaliq_pipeline.monitoring`)

```python
class WorkflowMonitor:
    """Track workflow execution with configurable detail levels."""
    
    def setup_logging(self, level: str, avoid_overload: bool = True) -> Logger:
        """Configurable logging - multiple levels to avoid information overload."""
        
    def track_progress(self, workflow_id: str) -> ProgressIndicator:
        """Real-time updates for long-running experiments."""
        
    def capture_errors(self, error: Exception, context: Dict) -> ErrorReport:
        """Detailed error reporting with context preservation."""
        
    def record_execution_metadata(self, workflow: Workflow) -> ExecutionMetadata:
        """Track timing, resource usage, and workflow history."""
```

### Phase 2 Components (Month 2: Research Integration)

#### 5. External Package Integration (`causaliq_pipeline.plugins`)

```python
class PluginManager:
    """Manages integration with R, Java, and Python packages."""
    
    def discover_packages(self) -> List[ExternalPackage]:
        """Automatic detection of available external packages."""
        
    def validate_dependencies(self, required_packages: List[str]) -> ValidationResult:
        """Check required packages before workflow execution."""
        
    def execute_external(self, package: str, method: str, params: Dict) -> Result:
        """Robust handling of external package failures."""

class RBnlearnPlugin:
    """Execute R bnlearn algorithms from Python workflows."""
    
    def check_r_environment(self) -> bool:
        """Verify R and bnlearn availability."""
        
    def execute_bnlearn_algorithm(self, algorithm: str, data: pd.DataFrame, 
                                 params: Dict) -> NetworkResult:
        """Execute bnlearn algorithm with standardized result format."""

class JavaTetradPlugin:
    """Integration with Java-based Tetrad algorithms."""
    
    def check_java_environment(self) -> bool:
        """Verify Java and Tetrad availability."""
        
    def execute_tetrad_algorithm(self, algorithm: str, data: pd.DataFrame,
                               params: Dict) -> NetworkResult:
        """Execute Tetrad algorithm with error handling."""
```

#### 6. Dataset Management (`causaliq_pipeline.datasets`)

```python
class DatasetManager:
    """Handles dataset download, randomization, and caching."""
    
    def cache_dataset(self, dataset: Dataset, cache_key: str) -> LocalDataset:
        """Local storage and reuse of downloaded datasets."""
        
    def apply_randomization(self, dataset: Dataset, config: RandomizationConfig) -> Dataset:
        """Subsampling, variable reordering, noise injection."""
        
    def track_dataset_metadata(self, dataset: Dataset) -> DatasetMetadata:
        """Track dataset versions and transformations."""
        
    def download_from_zenodo(self, dataset_id: str) -> LocalDataset:
        """Integration with zenodo-sync for dataset retrieval."""
```

#### 7. LLM Integration Hooks (`causaliq_pipeline.llm`)

```python
class LLMIntegrationManager:
    """Framework for LLM-guided model averaging and analysis."""
    
    def setup_model_averaging_coordination(self) -> ModelAveragingCoordinator:
        """Framework for LLM-guided model averaging."""
        
    def create_hypothesis_generation_hooks(self) -> HypothesisGenerator:
        """Integration points for LLM hypothesis generation."""
        
    def setup_result_interpretation(self) -> ResultInterpreter:
        """LLM analysis of experimental results."""
        
    def configure_research_workflow_support(self) -> ResearchWorkflowSupport:
        """Specific features for May 2026 research paper."""
```

#### 8. Advanced Series Management (`causaliq_pipeline.analysis`)

```python
class SeriesAnalyzer:
    """Cross-series analysis and statistical testing."""
    
    def compare_across_series(self, series_list: List[str]) -> ComparisonResult:
        """Compare results across different algorithmic approaches."""
        
    def perform_statistical_tests(self, results: SeriesResults) -> StatisticalResult:
        """Built-in statistical significance testing."""
        
    def aggregate_results(self, experiments: List[Experiment]) -> AggregatedResult:
        """Combine and summarize results across experiments."""
        
    def group_experiments(self, criteria: Dict) -> ExperimentGroups:
        """Flexible organization of related experiments."""
```

### Phase 3 Components (Month 3: Production)

#### 9. Workflow Management (`causaliq_pipeline.workflow`)

```python
class WorkflowExecutor:
    """Advanced workflow execution with pause/resume."""
    
    def pause_workflow(self, workflow_id: str) -> None:
        """Interrupt and restart long-running workflows."""
        
    def resume_workflow(self, workflow_id: str, checkpoint: Checkpoint) -> WorkflowResult:
        """Resume from checkpoint system - save intermediate state."""
        
    def manage_workflow_queue(self, workflows: List[Workflow]) -> QueueManager:
        """Manage multiple concurrent workflows."""
        
    def set_priority(self, workflow_id: str, priority: int) -> None:
        """Control execution order and resource allocation."""
```

#### 10. Resource Management (`causaliq_pipeline.resources`)

```python
class ResourceManager:
    """Comprehensive resource monitoring and limits."""
    
    def apply_runtime_limits(self, workflow: Workflow, limit: timedelta) -> None:
        """Configurable time limits per experiment/workflow."""
        
    def monitor_memory_usage(self, workflow_id: str) -> MemoryMetrics:
        """Track and limit memory usage."""
        
    def scale_resources(self, requirements: ResourceRequirements) -> ScalingResult:
        """Dynamic allocation based on workflow requirements."""
        
    def prioritize_jobs(self, queue: WorkflowQueue) -> PrioritizedQueue:
        """Intelligent scheduling of experiments."""
```

#### 11. Robust Error Handling (`causaliq_pipeline.errors`)

```python
class ErrorHandler:
    """Production-grade error handling and recovery."""
    
    def implement_fault_tolerance(self, workflow: Workflow) -> FaultTolerantWorkflow:
        """Continue execution when individual experiments fail."""
        
    def setup_auto_retry(self, max_retries: int, backoff_strategy: str) -> RetryManager:
        """Automatic retry with exponential backoff."""
        
    def enable_graceful_degradation(self, workflow: Workflow) -> GracefulWorkflow:
        """Provide partial results when possible."""
        
    def generate_diagnostics(self, error: Exception) -> DiagnosticReport:
        """Comprehensive error reporting and debugging info."""
```

#### 12. Results Management (`causaliq_pipeline.results`)

```python
class ResultsManager:
    """Standardized result storage replacing pickle files."""
    
    def store_experiment_result(self, experiment_id: str, result: ExperimentResult) -> None:
        """Store individual experiment result in standardized format."""
        
    def export_results(self, series_names: List[str], formats: List[str]) -> None:
        """Multiple output formats (CSV, JSON, HDF5)."""
        
    def track_algorithm_versions(self, algorithm: str) -> VersionInfo:
        """Track algorithm versions and parameter changes."""
        
    def ensure_reproducibility(self, experiment: Experiment) -> ReproducibilityPackage:
        """Complete metadata for result reproduction."""

@dataclass
class ExperimentResult:
    """Standardized experiment result format."""
    experiment_id: str
    algorithm: str
    hyperparameters: Dict
    dataset_info: DatasetMetadata
    learned_graph: nx.DiGraph
    algorithm_trace: List[GraphChange]
    metrics: Dict[str, float]  # SHD, precision, recall, BIC, AIC, F1
    runtime_info: RuntimeMetadata
    timestamp: datetime
```

## Series-Based Configuration Schema

### Basic Series Configuration
```yaml
metadata:
  name: "pc_vs_ges_comparison"
  description: "Compare PC and GES algorithms across datasets"

series:
  pc_experiments:
    algorithm: "pc"
    package: "causaliq-discovery"
    datasets:
      - name: "alarm"
        zenodo_id: "12345"
      - name: "asia" 
        zenodo_id: "12346"
    sample_sizes: [100, 500, 1000]
    randomizations: 10
    hyperparameters:
      alpha: [0.01, 0.05, 0.1]
    
  ges_experiments:
    algorithm: "ges"
    package: "causaliq-discovery"
    datasets: ["alarm", "asia"]  # Reference same datasets
    sample_sizes: [100, 500, 1000]
    randomizations: 10
    hyperparameters:
      score_type: ["bic", "aic"]

resources:
  max_parallel: 8
  memory_limit: "16GB"
  runtime_limit: "2h"
  
analysis:
  compare_series: ["pc_experiments", "ges_experiments"]
  metrics: ["shd", "precision", "recall", "bic", "f1"]
  statistical_tests: true
```

### Configuration Inheritance
```yaml
# base_experiment.yaml
metadata:
  name: "base_causal_discovery"

defaults:
  sample_sizes: [100, 500, 1000]
  randomizations: 10
  datasets: ["alarm", "asia"]

# specific_experiment.yaml  
inherits: "base_experiment.yaml"
metadata:
  name: "pc_specific_test"
  
overrides:
  algorithm: "pc"
  hyperparameters:
    alpha: 0.05
```

## Data Flow Architecture

```
YAML Config ──▶ ConfigurationManager ──▶ SeriesManager
     │                  │                      │
     ▼                  ▼                      ▼
Schema Validation   Parameter              Experiment
     │              Substitution           Expansion
     ▼                  │                      │
Dry-Run Preview        ▼                      ▼
     │            ValidationResult      TaskGraphBuilder
     ▼                  │                      │
Execution Plan         ▼                      ▼
                 WorkflowExecutor ◄────── DASK Graph
                       │                      │
                       ▼                      ▼
                 ResourceManager      ExternalPlugins
                       │                  (R/Java)
                       ▼                      │
                 ProgressMonitor              ▼
                       │               Algorithm Results
                       ▼                      │
                 ErrorHandler                ▼
                       │               ResultsManager
                       ▼                      │
                 CheckpointSystem             ▼
                                     StandardizedFormats
                                     (CSV/JSON/HDF5)
```

## Implementation Success Criteria

### Phase 1 (Month 1)
- ✅ Execute YAML-defined series workflows locally
- ✅ Validate configuration files with clear error messages  
- ✅ Generate and preview execution plans via dry-run
- ✅ Basic progress monitoring for multi-experiment workflows
- ✅ Configuration inheritance working for workflow templates

### Phase 2 (Month 2)
- ✅ R bnlearn and Python algorithms running in same workflow
- ✅ Automatic dataset download and caching from Zenodo
- ✅ Series-based experiments with randomization strategies
- ✅ LLM integration framework ready for research use
- ✅ Cross-series comparison and analysis capabilities

### Phase 3 (Month 3)
- ✅ Pause and resume complex multi-hour workflows
- ✅ Resource limits preventing runaway experiments
- ✅ Robust error handling with partial result preservation
- ✅ Production-ready standardized result formats
- ✅ Foundation complete for existing workflow migration

## Migration Strategy

### Gradual Transition
- Maintain existing monolithic workflows during development
- Implement new workflows in pipeline framework
- Migrate piece by piece with exact result validation
- Dual-system operation until migration complete

### Result Compatibility
- Standardized formats replace pickle files
- Exact numerical reproduction required
- Comprehensive testing against existing results
- Version tracking for algorithm implementations

This architecture directly implements the feature requirements from `feature_list.md`, ensuring systematic progress toward the May 2026 research goals while establishing the foundation for comprehensive workflow migration.