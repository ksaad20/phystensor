"""
phystensor: The Century-Proof Industrial Physics Engine.
Built for high-scalable inference, maritime compliance, EEE engineering, 
and multi-disciplinary research.

(c) 2026 Xylema Private Limited.
"""

# 1. CORE IDENTITY
# Primary classes and factory methods for rapid development.
from phystensor.core.tensor import PhysicalTensor
from phystensor.io.conversion import quantity

# 2. MODULE EXPOSURE
# Standard namespace access to sub-modules.
from phystensor import core
from phystensor import units
from phystensor import linalg
from phystensor import utils
from phystensor import io

# 3. UNIVERSAL PHYSICAL CONSTANTS
# High-precision constants for EEE, Aerospace, and Astrophysics.
from phystensor.units.constants import (
    c, G, h, e, k_B, N_A,      # Fundamental constants
    eps_0, mu_0, Z_0,         # EEE / Electromagnetics
    g_n, M_sun, AU            # Aerospace / Astrophysics
)

# 4. MATHEMATICAL CONSTANTS
# Dimensionless constants for rotations and engineering calculations.
from phystensor.utils.math_const import PI, TAU, E

# 5. SYSTEM METADATA
from phystensor.io.version import __version__, get_version_info

# 6. INDUSTRIAL ALIASES (Low-Labor API)
# 'q' is the industry standard for fast, unit-aware instantiation.
# 'tensor' provides a more descriptive alias for PhysicalTensor.
tensor = PhysicalTensor
q = quantity

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
