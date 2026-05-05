import numpy as np
from phystensor.core.tensor import PhysicalTensor
from phystensor.units.dimensions import Dimensions

class LinalgTester:
    """Verifies the mathematical and physical correctness of linalg outputs."""

    @staticmethod
    def assert_identity(tensor: PhysicalTensor):
        """Checks if a tensor is the identity matrix and is dimensionless."""
        # 1. Dimension Check
        if not all(v == 0 for v in tensor.dimensions.vector):
            raise AssertionError(f"Identity matrix must be dimensionless. Got: {tensor.dimensions}")
        
        # 2. Structure Check
        identity = np.eye(tensor.data.shape[0])
        if not np.allclose(tensor.data, identity):
            raise AssertionError("Matrix values do not match Identity structure.")
