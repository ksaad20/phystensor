from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar, Any, Protocol, runtime_checkable

import numpy as np

from phystensor.core.tensor import PhysicalTensor

# Generic Type for any class inheriting from PhysicalTensor.
# This allows 'PreserveDimensions' decorators to return the correct subclass.
PT = TypeVar("PT", bound=PhysicalTensor)

# A type representing any numeric input that can be vectorized by NumPy.
NumericData = float | int | np.ndarray | list

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
