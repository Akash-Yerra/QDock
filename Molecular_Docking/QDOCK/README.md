# QDock

A Python library for quantum-inspired molecular docking that encodes pose sampling as quadratic unconstrained binary optimization (QUBO) models solvable by quantum computers or classical annealers.

## Overview

QDock provides two complementary docking modes:

- **Feature Atom Matching (FAM)** – Feature-based matching with higher computational efficiency
- **Grid Point Matching (GPM)** – Grid-based matching with pose sampling performance close to Glide SP

## Key Features

- QUBO formulation of ligand–receptor pose sampling
- Two complementary docking strategies: FAM and GPM
- Integration with `pyqubo` and `neal` for simulated annealing-based QUBO solving
- Automatic preparation of ligands and receptors via AutoDockFR and OpenBabel
- Output of docking poses and match information for further analysis

## Installation

### From Git (recommended for now)

```bash
pip install git+https://github.com/allu0786ansari/QC_PROJECT.git
```

### Requirements

- **Python:** 3.9+ (3.11 tested)
- **Platform:** Linux / CentOS (recommended)

### Python Dependencies

Installed automatically with QDock:

- `pyqubo == 1.5.0`
- `prody >= 2.4.0`
- `numpy <2`
- `scipy == 1.10`
- `dwave-neal` (for the `neal` simulated annealer)

### External Dependencies

QDock requires the following command-line tools (must be installed manually):

#### AutoDockFR (ADFR Suite 1.0)

Provides: `prepare_ligand`, `prepare_receptor`, `autogrid4`

**Download and Extract ADFR Suite**

Download the Linux package: `ADFRsuite_x86_64Linux_1.0.tar.gz`
- Website: https://ccsb.scripps.edu/adfr/downloads/
- Google Drive: https://drive.google.com/drive/folders/13kMSGW0La6OooKCb5dqBMBEJ31AUfIw8?usp=sharing

Extract the archive:
```bash
tar -xvzf ADFRsuite_x86_64Linux_1.0.tar.gz
```

A new folder will appear: `ADFRsuite_x86_64Linux_1.0/`

**Add ADFR Suite to the System PATH**

Edit your `~/.bashrc`:
```bash
nano ~/.bashrc
```

Scroll to the bottom and add:
```bash
export PATH="$PATH:/home/<your_username>/ADFRsuite_x86_64Linux_1.0/bin"
```
*Replace `<your_username>` with your actual username*

Save the file: `Ctrl+O` → `Enter` → `Ctrl+X`

Reload the bash configuration:
```bash
source ~/.bashrc
```

**Verify ADFR Installation**

Run these commands to verify:
```bash
which prepare_receptor
which prepare_ligand
which adfr
```

**Note:** If installation is correct, each command should point inside the `ADFRsuite_x86_64Linux_1.0` folder

#### OpenBabel
Provides: `obabel` (used for PDBQT → PDB conversion)

Ensure these executables are on your `PATH`:

```bash
export PATH="$PATH:/path/to/autodockfr/bin"
export PATH="$PATH:/path/to/openbabel/bin"
```

## Usage

### Feature Atom Matching (FAM)

```python
from qdock import FAMDock

fam = FAMDock()

# 1. Prepare receptor (PDB)
fam.make_receptor("receptor.pdb")

# 2. Prepare ligands to dock
fam.make_ligand(["ligand1.mol2", "ligand2.mol2"])

# 3. Define docking box using a reference ligand
fam.make_box_ligand("ligand1.mol2")

# 4. Run docking
poses = fam.dock(
    edge_cutoff=1.0,
    K_dist=2.0,
    K_mono=2.0,
    n_pos=30,
    save_qubo=True,
    sim_dock=True,
    save_match=True,
    save_pose=True,
)
```

### Grid Point Matching (GPM)

```python
from qdock import GPMDock

gpm = GPMDock()

# 1. Prepare receptor (PDB)
gpm.make_receptor("receptor.pdb")

# 2. Prepare ligands to dock
gpm.make_ligand(["ligand1.mol2", "ligand2.mol2"])

# 3. Define docking box using a reference ligand
gpm.make_box_ligand(
    "ligand1.mol2",
    center_length=8.0,
    grid_length=1.0,
    cutoff=0.0,
)

# 4. Run docking
poses = gpm.dock(
    edge_cutoff=1.0,
    K_dist=2.0,
    K_mono=2.0,
    n_pos=30,
    save_qubo=True,
    sim_dock=True,
    save_match=True,
    save_pose=True,
)
```

### Output Structure

QDock creates the following output directories:

- `Ligands/` – Prepared ligand files
- `Box_Rawligand/` – Auxiliary ligand files for box definition
- `QUBOs/` – Saved QUBO matrices (`.npy`)
- `Matches/` – Match information (`.npy`)
- `Poses/` – Resulting poses (`.pdb`)

## Project Structure

```
qdock/
├── pyproject.toml
├── README.md
├── LICENSE
└── src/
    └── qdock/
        ├── __init__.py
        ├── feature_atom_matching/
        │   ├── __init__.py
        │   ├── famligand.py
        │   ├── famreceptor.py
        │   └── qdock.py          # FAMDock
        └── grid_point_matching/
            ├── __init__.py
            ├── gpmgrid.py
            ├── gpmligand.py
            ├── gpmreceptor.py
            └── qdock.py          # GPMDock
```

## Development

### Editable Install

```bash
git clone https://github.com/allu0786ansari/QC_PROJECT.git
cd QC_PROJECT
pip install -e .[dev]
```

The `[dev]` extra installs development dependencies such as `pytest`, `black`, and `mypy`.

### Running Tests

```bash
pytest
```
## Experimentation

### Setting Up Conda Environment for QDock

QDock requires older versions of NumPy & SciPy because it uses deprecated functions.

**Create Python 3.11 Environment**
```bash
conda create -n dockvenv python=3.11 -y
conda activate dockvenv
```

**Install Required Packages**
```bash
pip install 'numpy<2' 'scipy==1.10'
pip install prody pyqubo dimod dwave-samplers
```

These versions prevent compatibility issues when running QDock functions.

### Installing Jupyter Notebook and ipykernel

**Install Jupyter Notebook**
```bash
pip install notebook
```

**Install ipykernel for this environment**
```bash
pip install ipykernel
python -m ipykernel install --user --name dockvenv --display-name "Python (dockvenv)"
```

**Launch Notebook**
```bash
jupyter notebook
```

Inside Jupyter:
- Select **Kernel** → **Change kernel** → **Python (dockvenv)**

## Citation

If you use QDock in academic work, please cite:

> Jinyin Zha et al., *QDock*, Journal of Chemical Theory and Computation (2023).  
> https://doi.org/10.1021/acs.jctc.3c00943

## License

QDock is released under the **MIT License**.


Copyright (c) 2025 Allaudin Ansari

