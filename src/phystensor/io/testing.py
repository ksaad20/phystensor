import numpy as np
from phystensor.core.tensor import PhysicalTensor

class PhysicsTester:
    """
    Utility class for unit testing physical tensors.
    Used to verify that your 'Century-Proof' logic holds up under edge cases.
    """

    @staticmethod
    def assert_close(actual: PhysicalTensor, expected: PhysicalTensor, rel_tol: float = 1e-9):
        """
        Asserts that two tensors are physically identical 
        (both in data value and dimensional vector).
        """
        # 1. Dimension Check
        if actual.dimensions != expected.dimensions:
            raise AssertionError(
                f"DIMENSION MISMATCH: Actual {actual.dimensions.vector} "
                f"!= Expected {expected.dimensions.vector}"
            )
        
        # 2. Value Check (handling floating point noise)
        if not np.allclose(actual.data, expected.data, rtol=rel_tol):
            diff = np.abs(actual.data - expected.data)
            raise AssertionError(f"VALUE MISMATCH: Max difference {np.max(diff)}")

    @staticmethod
    def assert_dimensionless(tensor: PhysicalTensor):
        """Ensures a result has successfully collapsed to a dimensionless state."""
        if not all(v == 0 for v in tensor.dimensions.vector):
            raise AssertionError(f"EXPECTED DIMENSIONLESS: Got {tensor.dimensions.vector}")
