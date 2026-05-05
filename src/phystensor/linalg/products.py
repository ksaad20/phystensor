import numpy as np
from phystensor.core.tensor import PhysicalTensor

class PhysicsProducts:
    """Universal physical product engine."""

    @staticmethod
    def dot(a: PhysicalTensor, b: PhysicalTensor) -> PhysicalTensor:
        """Matrix/Vector multiplication. Resulting dim = dim(a) + dim(b)."""
        res_data = np.dot(a.data, b.data)
        return PhysicalTensor(res_data, a.dimensions + b.dimensions)

    @staticmethod
    def cross(a: PhysicalTensor, b: PhysicalTensor) -> PhysicalTensor:
        """3D Vector Cross Product. Vital for Torque and Magnetic Fields."""
        if a.data.shape[-1] != 3 or b.data.shape[-1] != 3:
            raise ValueError("Cross product requires 3D vectors.")
        res_data = np.cross(a.data, b.data)
        return PhysicalTensor(res_data, a.dimensions + b.dimensions)

    @staticmethod
    def outer(a: PhysicalTensor, b: PhysicalTensor) -> PhysicalTensor:
        """Outer product resulting in a higher-rank tensor."""
        res_data = np.outer(a.data, b.data)
        return PhysicalTensor(res_data, a.dimensions + b.dimensions)
