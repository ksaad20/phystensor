from __future__ import annotations

import numpy as np


class Dimensions:
    """Physical dimensions as a 7-vector (L, M, T, I, Θ, N, J)."""

    def __init__(
        self,
        vector: tuple[int, ...] | list[int] | np.ndarray,
    ) -> None:
        self.vector = tuple(int(v) for v in vector)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dimensions):
            return NotImplemented
        return self.vector == other.vector

    def __hash__(self) -> int:
        return hash(self.vector)

    def __add__(self, other: Dimensions) -> Dimensions:
        if not isinstance(other, Dimensions):
            return NotImplemented
        return Dimensions(
            tuple(a + b for a, b in zip(self.vector, other.vector))
        )

    def __sub__(self, other: Dimensions) -> Dimensions:
        if not isinstance(other, Dimensions):
            return NotImplemented
        return Dimensions(
            tuple(a - b for a, b in zip(self.vector, other.vector))
        )

    def __mul__(self, other: Dimensions) -> Dimensions:
        if not isinstance(other, Dimensions):
            return NotImplemented
        return Dimensions(
            tuple(a + b for a, b in zip(self.vector, other.vector))
        )

    def __truediv__(self, other: Dimensions) -> Dimensions:
        if not isinstance(other, Dimensions):
            return NotImplemented
        return Dimensions(
            tuple(a - b for a, b in zip(self.vector, other.vector))
        )

    def __pow__(self, exp: int | float) -> Dimensions:
        return Dimensions(tuple(int(a * exp) for a in self.vector))

    def __neg__(self) -> Dimensions:
        return Dimensions(tuple(-a for a in self.vector))

    def __repr__(self) -> str:
        return f"Dimensions({self.vector})"
