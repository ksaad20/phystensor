from __future__ import annotations

import numpy as np

from phystensor.units.dimensions import Dimensions
from phystensor.core.exceptions import DimensionalityError


class PhysicalTensor:
    """
    A high-performance wrapper for NumPy arrays that enforces
    dimensional consistency across all physical domains.
    """

    __array_priority__ = 1000.0

    def __init__(self, data, dimensions: Dimensions) -> None:
        """
        Initialize a physical tensor.

        Scalars are kept as Python scalars for natural behavior
        (e.g., round(), comparisons), while arrays remain NumPy arrays.
        """
        if isinstance(data, np.ndarray) and data.ndim == 0:
            data = data.item()

        if np.isscalar(data):
            self.data = data
        else:
            self.data = np.asanyarray(data)

        self.dimensions = dimensions

    def __repr__(self) -> str:
        return f"PT({self.data}, dim={self.dimensions.vector})"

    # --- NumPy Interoperability ---

    def __array__(self):
        return np.asarray(self.data)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        """
        Allows NumPy operations while preserving physical dimensions.
        """

        if method != "__call__":
            return NotImplemented

        raw_inputs = []
        dims = None

        for item in inputs:
            if isinstance(item, PhysicalTensor):
                raw_inputs.append(item.data)

                if dims is None:
                    dims = item.dimensions

                elif (
                    dims != item.dimensions
                    and ufunc.__name__ in ("add", "subtract")
                ):
                    raise DimensionalityError(
                        f"Dimensional mismatch in {ufunc.__name__}"
                    )
            else:
                raw_inputs.append(item)

        result = ufunc(*raw_inputs, **kwargs)

        if ufunc.__name__ in ("add", "subtract"):
            return PhysicalTensor(result, dims)

        if ufunc.__name__ == "multiply":
            tensors = [
                item for item in inputs if isinstance(item, PhysicalTensor)
            ]

            if len(tensors) == 2:
                new_dims = tensors[0].dimensions * tensors[1].dimensions
                return PhysicalTensor(result, new_dims)

            return PhysicalTensor(result, dims)

        if ufunc.__name__ == "divide":
            tensors = [
                item for item in inputs if isinstance(item, PhysicalTensor)
            ]

            if len(tensors) == 2:
                new_dims = tensors[0].dimensions / tensors[1].dimensions
                return PhysicalTensor(result, new_dims)

            return PhysicalTensor(result, dims)

        return result

    # --- Comparison Operators ---

    def __lt__(self, other: PhysicalTensor) -> bool:
        if self.dimensions != other.dimensions:
            raise DimensionalityError(
                "Cannot compare different physical quantities."
            )

        return self.data < other.data

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PhysicalTensor):
            return False

        return (
            self.dimensions == other.dimensions
            and np.array_equal(self.data, other.data)
        )

    # --- Core Arithmetic ---

    def __add__(self, other: PhysicalTensor) -> PhysicalTensor:
        if self.dimensions != other.dimensions:
            raise DimensionalityError(
                f"Cannot add quantities with dimensions "
                f"{self.dimensions} and {other.dimensions}"
            )

        return PhysicalTensor(
            self.data + other.data,
            self.dimensions,
        )

    def __sub__(self, other: PhysicalTensor) -> PhysicalTensor:
        if self.dimensions != other.dimensions:
            raise DimensionalityError(
                f"Cannot subtract quantities with dimensions "
                f"{self.dimensions} and {other.dimensions}"
            )

        return PhysicalTensor(
            self.data - other.data,
            self.dimensions,
        )

    def __mul__(self, other):
        if isinstance(other, PhysicalTensor):
            return PhysicalTensor(
                self.data * other.data,
                self.dimensions * other.dimensions,
            )

        return PhysicalTensor(
            self.data * other,
            self.dimensions,
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, PhysicalTensor):
            return PhysicalTensor(
                self.data / other.data,
                self.dimensions / other.dimensions,
            )

        return PhysicalTensor(
            self.data / other,
            self.dimensions,
        )

    # --- Advanced Math ---

    def __pow__(self, exponent: int | float) -> PhysicalTensor:
        new_vector = tuple(
            dimension * exponent
            for dimension in self.dimensions.vector
        )

        return PhysicalTensor(
            self.data ** exponent,
            Dimensions(new_vector),
        )

    def sqrt(self) -> PhysicalTensor:
        return self.__pow__(0.5)

    # --- Shape & Utility ---

    @property
    def shape(self) -> tuple[int, ...]:
        if hasattr(self.data, "shape"):
            return self.data.shape

        return ()

    @property
    def T(self) -> PhysicalTensor:  # noqa: N802
        """Transposition preserves physical dimensions."""
        return PhysicalTensor(self.data.T, self.dimensions)
