from typing import TypeVar, Union, Callable, Any, Protocol, runtime_checkable
import numpy as np

# Generic Type for any class inheriting from PhysicalTensor.
# This allows 'PreserveDimensions' decorators to return the correct subclass.
PT = TypeVar("PT", bound="PhysicalTensor")

# A type representing any numeric input that can be vectorized by NumPy.
NumericData = Union[float, int, np.ndarray, list]

# A function that performs a mathematical transformation while 
# maintaining the physical identity of the data.
PhysicsTransform = Callable[[np.ndarray], np.ndarray]

@runtime_checkable
class NumericScalable(Protocol):
    """
    A Protocol for objects that support basic linear scaling.
    Useful for validating external plugins before they enter the registry.
    """
    def __mul__(self, other: float) -> Any: ...
    def __truediv__(self, other: float) -> Any: ...
