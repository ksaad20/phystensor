from phystensor.linalg.products import PhysicsProducts as prod
from phystensor.linalg.norms import PhysicsNorms as norm
from phystensor.linalg.decompositions import PhysicsDecomp as decomp
from phystensor.linalg.solvers import PhysicsSolvers as solve
from phystensor.linalg.version import __linalg_version__

# Functional aliases for a cleaner API
dot = prod.dot
cross = prod.cross
inv = solve.inv
eig = decomp.eig
svd = decomp.svd

__all__ = [
    "dot", "cross", "inv", "eig", "svd", "prod", "norm", "decomp", "solve", "__linalg_version__"
]
