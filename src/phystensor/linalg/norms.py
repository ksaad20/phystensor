import numpy as np
from phystensor.core.tensor import PhysicalTensor

class PhysicsNorms:
    """Calculates the 'magnitude' of physical quantities."""

    @staticmethod
    def norm(tensor: PhysicalTensor, ord: int = 2) -> PhysicalTensor:
        """
        Calculates the L2 (Euclidean) or other norms.
        The result maintains the physical units of the input.
        """
        res_data = np.linalg.norm(tensor.data, ord=ord)
        return PhysicalTensor(res_data, tensor.dimensions)

    @staticmethod
    def trace(tensor: PhysicalTensor) -> PhysicalTensor:
        """The sum of diagonal elements (e.g., for stress tensors)."""
        res_data = np.trace(tensor.data)
        return PhysicalTensor(res_data, tensor.dimensions)
