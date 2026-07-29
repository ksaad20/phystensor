from typing import Any
import numpy as np
from phystensor.core.exceptions import DimensionalityError

class PhysicalOOPS:
    """
    Implements Object-Oriented Physics Safeguards.
    Ensures that 'naked' numbers cannot be added to 'clothed' tensors.
    """

    @staticmethod
    def validate_scalar_op(op_name: str, other: Any):
        """
        Prevents adding a raw float/int to a PhysicalTensor.
        Multiplying is allowed (scaling), but adding is physically undefined.
        """
        if op_name in ['add', 'sub', 'radd', 'rsub']:
            if not hasattr(other, 'dimensions'):
                raise DimensionalityError(
                    f"Cannot {op_name} a dimensionless scalar to a unit-bearing tensor. "
                    "Use pt.q(val, 'unit') to wrap the scalar first."
                )
