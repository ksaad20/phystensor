from __future__ import annotations

from typing import Any, Protocol, TypeVar, runtime_checkable

import numpy as np


# Type alias for any data that can be converted into a PhysicalTensor
TensorLike = np.ndarray | list | float | int

# Shape type for multi-dimensional arrays
Shape = tuple[int, ...]

# Ordered SI Vector: [L, M, T, I, Θ, N, J]
SIVector = tuple[int, int, int, int, int, int, int]


@runtime_checkable
class PhysicalObject(Protocol):
    """A protocol for any object that carries physical dimensions."""

    dimensions: Any
    data: np.ndarray
