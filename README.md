# causaliq-pipeline

[![Python Support](https://img.shields.io/pypi/pyversions/zenodo-sync.svg)](https://pypi.org/project/zenodo-sync/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a template for **creating new CausalIQ repos** which provides a new **capability** and follows CausalIQ development practices.

## Status

🚧 **Active Development** - This repository is currently in active development. It will be updated periodically to align with the latest approaches used in CausalIQ repos. New repos within the CausalIQ project should follow the naming convention causaliq-[capability], e.g. "causaliq-discovery" or "causaliq-analysis".


## Features

- 📁 **Standardised project structure**: following current best practices
- ⌨️ **CLI Interface**: An initial dummy command-line interface.
- 📖 **Documentation framework**: using mkdocs with shared CausalIQ branding.
- 🐍 **Python setup**: providing virtual environments for Python 3.9, 3.10, 3.11 and 3.12.
- 🔬 **pytest test framework**: for unit, functional and integration testing including code coverage.
- 🔄 **Continuous Integration testing**: across Python versions and operating systems using GitHub actions 


## New CausalIQ repo creation

This section provides instructions for **creating a completely new CausalIQ repo** which offers a **new capability**. This capability will be referred to as "newcapability" in the following instructions below, but should in practice be a word which meaningfully summarises the capability e.g. "pipeline" or "score".

### Prerequisites

- Git 
- Latest stable versions of Python 3.9, 3.10. 3.11 and 3.12

### Create the new repo on GitHub

- Create the new repo with name causaliq-newcapability specifying **this repository (i.e. causaliq-pipeline) as the template** with an initial commit message "feat: initial project setup from causaliq-pipeline"

### Clone the new repo locally and check that it works

Clone the causaliq-newcapability repo locally as normal

```bash
git clone https://github.com/causaliq/causaliq-newcapability.git
```

Set up the Python virtual environments and activate the Python v3.11 virtual environment.

```text
scripts/setup-env -Install
scripts/activate 311
```

Check that the causaliq-pipeline CLI is working, check that all CI tests pass, and start up the local mkdocs webserver. There should be no errors  reported in any of these.

```text
causaliq-pipeline --help
scripts/check_ci
mkdocs serve
```

Enter **http://127.0.0.1:8000/** in a browser and check that the 
causaliq-pipeline skeleton documentation is visible.

### Change all references in package to new package name

In the IDE (e.g. VSCode) editor make the following GLOBAL changes to all files and folder names

- replace **causaliq-pipeline** with **causaliq-newcapability** in all files
- replace **causaliq_pipeline** with **causaliq_newcapability** in all files
- rename folder **src/causaliq_pipeline** to **src/causaliq_newcapability**
- manually delete all folders under venv (which will contain references to the causaliq-pipeline)

⚠️ **Important**: Make sure to use underscores for Python package names (`causaliq_newcapability`) and hyphens for repo names (`causaliq-newcapability`)

### Check newly named package works OK and commit to GitHub

- Setup the virtual environments again (which will now contain the package causaliq-newcapability), and check CI testing works with te renamed package

```powershell
scripts/setup-env -Install
scripts/check_ci
```

If all is OK, commit this to GitHub with message "refactor: package name changed to causaliq-newcapability"


### Start work on new package

Begin implementing the functionality of this new CausalIQ package.

### Checklist
- [ ] GitHub repo created from template
- [ ] Repo cloned locally
- [ ] Initial tests pass
- [ ] All references renamed
- [ ] Folder renamed
- [ ] venv folders deleted
- [ ] Final tests pass
- [ ] Changes committed


---

**Supported Python Versions**: 3.9, 3.10, 3.11, 3.12  
**Default Python Version**: 3.11
