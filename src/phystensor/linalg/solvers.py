import numpy as np
from phystensor.core.tensor import PhysicalTensor

class PhysicsSolvers:
    """Solves physical systems of equations."""

    @staticmethod
    def solve(a: PhysicalTensor, b: PhysicalTensor) -> PhysicalTensor:
        """
        Solves Ax = B for x.
        Dimension logic: dim(x) = dim(b) - dim(a).
        """
        res_data = np.linalg.solve(a.data, b.data)
        return PhysicalTensor(res_data, b.dimensions - a.dimensions)

    @staticmethod
    def inv(tensor: PhysicalTensor) -> PhysicalTensor:
        """
        Matrix inversion.
        Dimension logic: Result is the reciprocal (negated vector).
        """
        res_data = np.linalg.inv(tensor.data)
        new_vec = tuple(-v for v in tensor.dimensions.vector)
        return PhysicalTensor(res_data, Dimensions(new_vec))

    @staticmethod
    def det(tensor: PhysicalTensor) -> PhysicalTensor:
        """
        Determinant. 
        Dimension logic: dim(det) = dim(tensor) * N (where N is matrix order).
        """
        order = tensor.data.shape[0]
        res_data = np.linalg.det(tensor.data)
        new_vec = tuple(v * order for v in tensor.dimensions.vector)
        return PhysicalTensor(res_data, Dimensions(new_vec))
