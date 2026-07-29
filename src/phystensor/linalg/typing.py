from __future__ import annotations

from typing import Any, TypeVar

import numpy as np


# Type for matrices that must be square for certain linalg ops (inv, det, eig)
SquareMatrix = np.ndarray  # Used for documentation/hints

# Result of a decomposition (e.g., Eigen or SVD)
DecompResult = tuple[Any, Any]

# Axis specification for norms and products
Axis = int | tuple[int, ...]
