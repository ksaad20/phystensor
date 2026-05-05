from typing import Union, List, Tuple, TypeVar, Protocol, runtime_checkable
import numpy as np

# Type alias for any data that can be converted into a PhysicalTensor
TensorLike = Union[np.ndarray, List, float, int]

# Shape type for multi-dimensional arrays
Shape = Tuple[int, ...]

# Ordered SI Vector: [L, M, T, I, Θ, N, J]
SIVector = Tuple[int, int, int, int, int, int, int]

@runtime_checkable
class PhysicalObject(Protocol):
    """A protocol for any object that carries physical dimensions."""
    dimensions: Any
    data: np.ndarray
