"""QDock: Quantum-enhanced pose sampling for molecular docking.

This package encodes pose sampling as QUBO models suitable for quantum
computers, providing two main methods:
- Grid Point Matching (GPM)
- Feature Atom Matching (FAM)
"""

# Package version (used by pyproject.toml via [tool.hatch.version])
__version__ = "0.1.0"

# We intentionally do NOT import subpackages here to avoid circular imports.
# Use:
#   from qdock.feature_atom_matching import FAMDock
#   from qdock.grid_point_matching import GPMDock

__all__ = ["__version__"]
