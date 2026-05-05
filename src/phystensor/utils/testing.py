import numpy as np
from phystensor.core.tensor import PhysicalTensor
from phystensor.units.dimensions import Dimensions

class SyntheticData:
    """Generates valid physical tensors for unit testing and benchmarking."""
    
    @staticmethod
    def create_random(dims: Dimensions, shape: tuple = (10, 10)) -> PhysicalTensor:
        """Creates a tensor with random values but fixed dimensions."""
        data = np.random.rand(*shape)
        return PhysicalTensor(data, dims)

    @staticmethod
    def create_identity_mass(shape: tuple = (3, 3)) -> PhysicalTensor:
        """Helper for creating a mass-dimension tensor for EEE/Maritime tests."""
        return PhysicalTensor(np.eye(*shape), Dimensions((0, 1, 0, 0, 0, 0, 0)))
