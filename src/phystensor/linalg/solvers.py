from __future__ import annotations

import numpy as np

from phystensor.core.tensor import PhysicalTensor
from phystensor.units.dimensions import Dimensions


class PhysicsSolvers:
    """Solves physics-aware systems of equations."""

    def __init__(self, *args, **kwargs) -> None:
        pass

    @staticmethod
    def solve(a: PhysicalTensor, b: PhysicalTensor) -> PhysicalTensor:
        """
        Solves Ax = B for x.

        Dimension logic:
            dim(x) = dim(b) / dim(a)
        """
        # Scalar case (e.g. Ohm's law: I = V / R)
        if np.ndim(a.data) < 2 and np.ndim(b.data) < 2:
            res_data = b.data / a.data
        else:
            res_data = np.linalg.solve(a.data, b.data)

        return PhysicalTensor(
            res_data,
            b.dimensions / a.dimensions,
        )

    @staticmethod
    def inv(tensor: PhysicalTensor) -> PhysicalTensor:
        res_data = np.linalg.inv(tensor.data)
        new_vec = tuple(-value for value in tensor.dimensions.vector)
        return PhysicalTensor(res_data, Dimensions(new_vec))

    @staticmethod
    def det(tensor: PhysicalTensor) -> PhysicalTensor:
        order = tensor.data.shape[0]
        res_data = np.linalg.det(tensor.data)
        new_vec = tuple(value * order for value in tensor.dimensions.vector)
        return PhysicalTensor(res_data, Dimensions(new_vec))
