from typing import Union, Tuple, TypeVar, Any
import numpy as np

# Type for matrices that must be square for certain linalg ops (inv, det, eig)
SquareMatrix = np.ndarray  # Used for documentation/hints

# Result of a decomposition (e.g., Eigen or SVD)
DecompResult = Tuple[Any, Any]

# Axis specification for norms and products
Axis = Union[int, Tuple[int, ...]]
