from __future__ import annotations

import numpy as np

from phystensor.units.dimensions import Dimensions
from phystensor.core.exceptions import DimensionalityError


class PhysicalTensor:
    """
    A high-performance wrapper for NumPy arrays that enforces 
    dimensional consistency across all physical domains.
    """
    __array_priority__ = 1000.0  # Forces NumPy to defer to our __array_ufunc__

    def __init__(self, data, dimensions: Dimensions) -> None:
        # Convert 0-d arrays to Python scalars so round() works on them
        if isinstance(data, np.ndarray) and data.ndim == 0:
            data = data.item()
        self.data = np.asanyarray(data)
        self.dimensions = dimensions

    def __repr__(self) -> str:
        return f"PT({self.data}, dim={self.dimensions.vector})"

    # --- NumPy Interoperability ---
    def __array__(self):
        return self.data

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        """
        The Secret Sauce: This allows NumPy functions (like np.add) 
        to work directly on PhysicalTensors while maintaining units.
        """
        if method != '__call__':
            return NotImplemented

        # Extract raw data and validate dimensions
        raw_inputs = []
        dims = None
        
        for x in inputs:
            if isinstance(x, PhysicalTensor):
                raw_inputs.append(x.data)
                if dims is None:
                    dims = x.dimensions
                elif dims != x.dimensions and ufunc.__name__ in ['add', 'subtract']:
                    raise DimensionalityError(
                        f"Dimensional Mismatch in {ufunc.__name__}"
                    )
            else:
                raw_inputs.append(x)

        # Execute the math
        result = ufunc(*raw_inputs, **kwargs)

        # Handle Dimension Propagation
        if ufunc.__name__ in ('add', 'subtract'):
            return PhysicalTensor(result, dims)
        elif ufunc.__name__ == 'multiply':
            # Multiply dimensions (add exponents)
            pt_inputs = [x for x in inputs if isinstance(x, PhysicalTensor)]
            if len(pt_inputs) == 2:
                new_dims = pt_inputs[0].dimensions * pt_inputs[1].dimensions
                return PhysicalTensor(result, new_dims)
            return PhysicalTensor(result, dims)
        elif ufunc.__name__ == 'divide':
            pt_inputs = [x for x in inputs if isinstance(x, PhysicalTensor)]
            if len(pt_inputs) == 2:
                new_dims = pt_inputs[0].dimensions / pt_inputs[1].dimensions
                return PhysicalTensor(result, new_dims)
            return PhysicalTensor(result, dims)
        
        return result

    # --- Comparison Operators (Logic) ---
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
        return PhysicalTensor(self.data + other.data, self.dimensions)

    def __sub__(self, other: PhysicalTensor) -> PhysicalTensor:
        if self.dimensions != other.dimensions:
            raise DimensionalityError(
                f"Cannot subtract quantities with dimensions "
                f"{self.dimensions} and {other.dimensions}"
            )
        return PhysicalTensor(self.data - other.data, self.dimensions)

    def __mul__(self, other):
        if isinstance(other, PhysicalTensor):
            # Multiplication: dimensions combine (exponents add)
            return PhysicalTensor(
                self.data * other.data,
                self.dimensions * other.dimensions,
            )
        return PhysicalTensor(self.data * other, self.dimensions)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, PhysicalTensor):
            # Division: dimensions divide (exponents subtract)
            return PhysicalTensor(
                self.data / other.data,
                self.dimensions / other.dimensions,
            )
        return PhysicalTensor(self.data / other, self.dimensions)

    # --- Advanced Math ---
    def __pow__(self, exponent: int | float) -> PhysicalTensor:
        # Every element in the dimension vector is scaled by the exponent
        new_vec = tuple(d * exponent for d in self.dimensions.vector)
        return PhysicalTensor(self.data ** exponent, Dimensions(new_vec))

    def sqrt(self) -> PhysicalTensor:
        return self.__pow__(0.5)

    # --- Shape & Utility ---
    @property
    def shape(self) -> tuple[int, ...]:
        return self.data.shape

    @property
    def T(self) -> PhysicalTensor:
        """Transposition preserves dimensions."""
        return PhysicalTensor(self.data.T, self.dimensions)
