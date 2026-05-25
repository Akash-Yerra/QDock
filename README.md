# QDock: Quantum-Inspired Molecular Docking using QUBO Optimization

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-research-orange)

QDock is a quantum-inspired molecular docking framework that formulates protein–ligand docking as a **Quadratic Unconstrained Binary Optimization (QUBO)** problem.

This project combines:

* molecular feature extraction
* feature atom mapping
* interaction graph generation
* QUBO construction
* optimization-ready docking workflows

to explore future compatibility with:

* classical optimizers
* simulated annealing
* D-Wave quantum annealers
* QAOA
* hybrid quantum-classical optimization

The repository demonstrates the complete computational pipeline from molecular preprocessing to docking pose generation and QUBO analysis.

---

# Motivation

Molecular docking is a fundamental computational problem in drug discovery used to predict how a ligand binds to a target protein.

Traditional docking approaches often rely on:

* heuristic search methods
* scoring functions
* stochastic optimization

However, docking becomes increasingly difficult as molecular complexity and conformational search spaces grow.

QUBO formulations provide a powerful mathematical framework for representing combinatorial optimization problems and naturally connect molecular docking with emerging quantum optimization systems.

This project explores the transformation of docking workflows into QUBO-based optimization pipelines that can later be solved using:

* classical annealing
* quantum annealing
* hybrid optimization algorithms

---

# Scientific Background

## Molecular Docking

Molecular docking attempts to determine:

* how a ligand binds to a receptor
* the optimal binding configuration
* energetically favorable interactions

The problem is highly combinatorial because many possible ligand–protein interaction configurations exist.

---

## What is QUBO?

QUBO stands for:

```math
Quadratic  Unconstrained  Binary  Optimization
```

A QUBO problem minimizes an objective function of binary variables:

```math
Q(x) = \sum_{i,j} Q_{ij} x_i x_j
```

where:

* (x_i) are binary decision variables
* (Q_{ij}) encodes interaction rewards and penalties

QUBO formulations are widely used in:

* quantum annealing
* combinatorial optimization
* scheduling
* graph problems
* quantum computing workflows

In this project, molecular interaction constraints are encoded into a QUBO matrix for optimization.

---

# Methodology

The QDock workflow follows the pipeline below:

```text
Protein + Ligand
        ↓
Feature Extraction
        ↓
Feature Atom Mapping (FAM)
        ↓
Interaction Graph Construction
        ↓
QUBO Generation
        ↓
Optimization Workflow
        ↓
Docking Pose Selection
        ↓
Final Docked Structures
```

---

# Feature Atom Mapping (FAM)

The Feature Atom Mapping module identifies chemically meaningful correspondences between:

* ligand atoms
* receptor atoms

based on:

* geometric consistency
* interaction compatibility
* molecular features

These mappings form the basis for interaction graph generation and QUBO construction.

---

# Interaction Graph Construction

The generated molecular mappings are transformed into an interaction graph where:

* nodes represent possible molecular correspondences
* edges represent compatibility relationships

This graph representation enables conversion into a binary optimization problem.

---

# QUBO Construction

The interaction graph is encoded into a QUBO matrix where:

* valid docking configurations receive rewards
* conflicting assignments receive penalties
* geometric constraints are preserved

The resulting QUBO formulation becomes optimization-ready for:

* simulated annealing
* classical optimizers
* quantum annealers
* QAOA workflows

---

# Experimental Workflow

The current implementation demonstrates the workflow using:

```text
PDB ID: 1Y6R
```

Included files:

* `1y6r_protein.pdb`
* `1y6r_ligand.mol2`

The workflow performs:

* molecular preprocessing
* feature extraction
* feature atom mapping
* QUBO generation
* docking structure preparation
* optimization-ready output generation

---

# Experimental Outputs

The workflow successfully generates:

* processed molecular structures
* mapping outputs
* docking pose candidates
* generated QUBO formulations
* interaction mappings
* optimization-ready terms

Generated outputs include:

* working directories
* processed receptor/ligand structures
* docking-related artifacts
* QUBO analysis files

---

# Why This Repository Structure Is Different

This repository intentionally contains both:

```text
PROJECT BEFORE EXECUTION
```

and

```text
PROJECT AFTER EXECUTION
```

structures.

The goal is to help:

* students
* beginners
* researchers
* quantum computing learners

understand the complete computational workflow lifecycle.

Instead of hiding generated outputs, this repository demonstrates:

* how the project looks before execution
* what files are generated after execution
* workflow progression
* intermediate computational artifacts

This educational workflow structure makes the project easier to study and reproduce.

---

# Repository Structure

```text
Molecular_Docking/
│
├── QDOCK/
│   ├── src/
│   ├── data/
│   ├── run_fam.py
│   ├── convert_qdock_to_terms.py
│   ├── pyproject.toml
│   ├── requirements-dev.txt
│   └── README.md
│
├── Example_run_of_QDOCK/
│   ├── workdir_fam/
│   ├── generated outputs
│   ├── docking results
│   ├── QUBO outputs
│   └── processed structures
│
└── notebooks/
```

---

# Understanding the Repository

## 1. `QDOCK/`

Contains the clean project before execution.

Includes:

* source code
* docking workflows
* QUBO generation logic
* scripts
* raw molecular structures

Represents:

```text
PROJECT BEFORE EXECUTION
```

---

## 2. `Example_run_of_QDOCK/`

Contains generated outputs after running the workflow.

Includes:

* working directories
* processed molecular structures
* generated QUBOs
* docking artifacts
* optimization-ready outputs

Represents:

```text
PROJECT AFTER EXECUTION
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd Molecular_Docking
```

---

## Create Environment

```bash
conda create -n qdock python=3.10
conda activate qdock
```

---

## Install Dependencies

```bash
pip install -e .
```

or

```bash
pip install -r requirements-dev.txt
```

---

# Main Dependencies

Main packages used:

* numpy
* scipy
* prody
* pyqubo
* dwave-neal

Additional dependencies may be required depending on:

* notebook workflows
* optimization backend
* docking utilities

---

# Running the Project

## Step 1 — Navigate to QDOCK

```bash
cd QDOCK
```

---

## Step 2 — Run Feature Atom Mapping Workflow

```bash
python run_fam.py
```

---

## Step 3 — Generated Outputs

Generated outputs will appear inside:

```text
workdir_fam/
```

including:

* processed molecules
* mapping outputs
* docking structures
* generated intermediate files

---

## Step 4 — Convert QUBO to Interaction Terms

```bash
python convert_qdock_to_terms.py
```

This converts generated QUBOs into optimization-analysis-ready interaction terms.

---

# Future Work

Future directions for this project include:

* D-Wave quantum annealing integration
* QAOA workflows
* hybrid quantum-classical optimization
* advanced scoring functions
* GPU acceleration
* automated benchmarking
* visualization tools
* larger docking datasets

---

# Educational Purpose

This repository is designed not only as a research implementation but also as a learning resource for:

* molecular docking
* QUBO optimization
* quantum computing
* quantum-inspired drug discovery

The project intentionally exposes:

* intermediate workflow stages
* generated outputs
* computational artifacts
* optimization formulations

to help learners understand the complete pipeline.

---

# Acknowledgements

This project was developed by extending and restructuring ideas from:

* https://github.com/allu0786ansari/QC_PROJECT
* https://github.com/allu0786ansari/Qubo_Analysis

with additional:

* workflow integration
* restructuring
* experimentation
* educational organization
* QUBO analysis workflows

---

# License

This project is licensed under the MIT License.

See:

```text
LICENSE
```

for details.

---

# Citation

If you use this repository in research or academic work, please cite the repository appropriately.

A future `CITATION.cff` file will also be included.

---

# Final Note

QDock aims to bridge:

```text
Computational Chemistry
        +
Quantum Optimization
        +
QUBO Modeling
```

while remaining understandable and educational for researchers and beginners entering the field of quantum-inspired drug discovery.
