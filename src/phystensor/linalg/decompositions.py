import numpy as np
from phystensor.core.tensor import PhysicalTensor
from phystensor.units.dimensions import Dimensions

class PhysicsDecomp:
    """Matrix decompositions that respect SI-base dimensions."""

    @staticmethod
    def eig(tensor: PhysicalTensor):
        """
        Eigen-decomposition. 
        Eigenvalues: Inherit the dimensions of the tensor.
        Eigenvectors: Dimensionless (normalized directions).
        """
        vals, vecs = np.linalg.eig(tensor.data)
        dimensionless = Dimensions((0,0,0,0,0,0,0))
        
        return (
            PhysicalTensor(vals, tensor.dimensions),
            PhysicalTensor(vecs, dimensionless)
        )

    @staticmethod
    def svd(tensor: PhysicalTensor):
        """Singular Value Decomposition for structural stability analysis."""
        u, s, vh = np.linalg.svd(tensor.data)
        dimensionless = Dimensions((0,0,0,0,0,0,0))
        
        return (
            PhysicalTensor(u, dimensionless),
            PhysicalTensor(s, tensor.dimensions), # Singular values carry the units
            PhysicalTensor(vh, dimensionless)
        )
