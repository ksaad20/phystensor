from __future__ import annotations

from phystensor.linalg.decompositions import PhysicsDecomp as decomp  # noqa: N813
from phystensor.linalg.norms import PhysicsNorms as norm  # noqa: N813
from phystensor.linalg.products import PhysicsProducts as prod  # noqa: N813
from phystensor.linalg.solvers import PhysicsSolvers as _PhysicsSolvers
from phystensor.linalg.version import __linalg_version__


# Functional aliases for a cleaner API
dot = prod.dot
cross = prod.cross
inv = _PhysicsSolvers.inv
eig = decomp.eig
svd = decomp.svd


def solve(a, b):
    """Solve a · x = b. Returns a PhysicalTensor."""
    return _PhysicsSolvers().solve(a, b)


__all__ = [
    "dot",
    "cross",
    "inv",
    "eig",
    "svd",
    "prod",
    "norm",
    "decomp",
    "solve",
    "__linalg_version__",
]
