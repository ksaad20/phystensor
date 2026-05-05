import numpy as np
from typing import Any, Union, Tuple
from phystensor.units.dimensions import Dimensions

class PhysicalTensor:
    """
    A high-performance wrapper for NumPy arrays that enforces 
    dimensional consistency across all physical domains.
    """
    __array_priority__ = 1000.0  # Forces NumPy to defer to our __array_ufunc__

    def __init__(self, data: Any, dimensions: Dimensions):
        self.data = np.asanyarray(data)
        self.dimensions = dimensions

    def __repr__(self):
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
                    raise TypeError(f"Dimensional Mismatch in {ufunc.__name__}")
            else:
                raw_inputs.append(x)

        # Execute the math
        result = ufunc(*raw_inputs, **kwargs)

        # Handle Dimension Propagation
        if ufunc.__name__ == 'add' or ufunc.__name__ == 'subtract':
            return PhysicalTensor(result, dims)
        elif ufunc.__name__ == 'multiply':
            # Logic for multiplying two different dims belongs in __mul__
            return NotImplemented 
        
        return result

    # --- Comparison Operators (Logic) ---
    def __lt__(self, other: 'PhysicalTensor') -> bool:
        if self.dimensions != other.dimensions:
            raise TypeError("Cannot compare different physical quantities.")
        return self.data < other.data

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PhysicalTensor): return False
        return self.dimensions == other.dimensions and np.array_equal(self.data, other.data)

    # --- Core Arithmetic ---
    def __add__(self, other: 'PhysicalTensor') -> 'PhysicalTensor':
        if self.dimensions != other.dimensions:
            raise TypeError(f"Mismatch: {self.dimensions} != {other.dimensions}")
        return PhysicalTensor(self.data + other.data, self.dimensions)

    def __sub__(self, other: 'PhysicalTensor') -> 'PhysicalTensor':
        if self.dimensions != other.dimensions:
            raise TypeError(f"Mismatch: {self.dimensions} != {other.dimensions}")
        return PhysicalTensor(self.data - other.data, self.dimensions)

    def __mul__(self, other: Any) -> 'PhysicalTensor':
        if isinstance(other, PhysicalTensor):
            return PhysicalTensor(self.data * other.data, self.dimensions + other.dimensions)
        return PhysicalTensor(self.data * other, self.dimensions)

    def __truediv__(self, other: Any) -> 'PhysicalTensor':
        if isinstance(other, PhysicalTensor):
            return PhysicalTensor(self.data / other.data, self.dimensions - other.dimensions)
        return PhysicalTensor(self.data / other, self.dimensions)

    # --- Advanced Math ---
    def __pow__(self, exponent: Union[int, float]) -> 'PhysicalTensor':
        # Every element in the dimension vector is scaled by the exponent
        new_vec = tuple(d * exponent for d in self.dimensions.vector)
        return PhysicalTensor(self.data ** exponent, Dimensions(new_vec))

    def sqrt(self) -> 'PhysicalTensor':
        return self.__pow__(0.5)

    # --- Shape & Utility ---
    @property
    def shape(self) -> Tuple[int, ...]:
        return self.data.shape

    @property
    def T(self) -> 'PhysicalTensor':
        """Transposition preserves dimensions."""
        return PhysicalTensor(self.data.T, self.dimensions)

from phystensor.io.logging import log_dimension_error

# Inside a check:
# In your __add__ or __sub__ method (or similar)
def __add__(self, other):
    # Ensure you are referencing the attributes of the current and other object
    dims_a = self.dimensions 
    dims_b = other.dimensions if hasattr(other, 'dimensions') else None

    if dims_a != dims_b: # This is line 110
        from phystensor.io.logging import log_dimension_error
        log_dimension_error(dims_a, dims_b)
    
    # ... rest of your logic
