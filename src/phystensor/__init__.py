"""
phystensor: The Century-Proof Industrial Physics Engine.
Built for high-scalable inference, maritime compliance, EEE engineering, 
and multi-disciplinary research.

(c) 2026 Xylema Private Limited.
"""

# 1. CORE IDENTITY (Lazy-loaded to prevent circularity)
def __getattr__(name):
    if name in ("PhysicalTensor", "tensor"):
        from phystensor.core.tensor import PhysicalTensor
        return PhysicalTensor
    if name in ("quantity", "q"):
        from phystensor.io.conversion import quantity
        return quantity
    
    # Standard Module Exposure
    if name == "core":
        import phystensor.core as core
        return core
    if name == "units":
        import phystensor.units as units
        return units
    # Repeat for linalg, utils, io...

    raise AttributeError(f"module {__name__} has no attribute {name}")

# Move Constants to absolute imports ONLY if they don't depend on PhysicalTensor
from phystensor.units.constants import (
    c, G, h, e, k_B, N_A, eps_0, mu_0, Z_0, g_n, M_sun, AU
)
from phystensor.utils.math_const import PI, TAU, E

__all__ = [
    "PhysicalTensor",
    "tensor",
    "quantity",
    "q",
    "core",
    "units",
    "linalg",
    "utils",
    "io",
    "c", "G", "h", "e", "k_B", "N_A",
    "eps_0", "mu_0", "Z_0",
    "g_n", "M_sun", "AU",
    "PI", "TAU", "E",
    "__version__",
    "get_version_info"
]

# 7. LOGGING & INITIALIZATION
import logging
import os

# Initialize industrial-grade logger
# Defaults to NullHandler to remain silent in production environments.
logger = logging.getLogger("phystensor")
logger.addHandler(logging.NullHandler())

# Optional diagnostic banner triggered by environment variable.
if os.getenv("PHYSTENSOR_VERBOSE") == "1":
    print(f"--- Phystensor Physics Engine v{__version__} ---")
    print(f"SI-Base DNA: 7-Tuple Vectorization Active")
    print(f"Industrial Backend: Operational")
