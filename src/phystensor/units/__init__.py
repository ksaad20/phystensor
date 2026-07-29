
"""
phystensor: The Century-Proof Industrial Physics Engine.
Built for high-scalable inference, maritime compliance, EEE engineering, 
and multi-disciplinary research.

(c) 2026 Xylema Private Limited.
"""

# 1. THE CORE IDENTITY
# Expose the primary class and the factory function for rapid development.
from phystensor.core.tensor import PhysicalTensor
from phystensor.io.conversion import quantity

# 2. THE NAMESPACE BRIDGE
# Allow users to access sub-modules directly (e.g., pt.linalg.solve).
from phystensor import core
from . import registry
from phystensor import linalg
from phystensor import utils
from phystensor import io

# 3. GLOBAL ENGINEERING CONSTANTS
# Direct access to the physics and math required for immediate calculation.
from phystensor.units.constants import (
    c, G, h, e, k_B, N_A,      # Fundamental
    eps_0, mu_0, Z_0,         # EEE / Electromagnetics
    g_n, M_sun, AU            # Aerospace / Astrophysics
)
from phystensor.utils.math_const import PI, TAU, E

# 4. SYSTEM METADATA
from phystensor.io.version import __version__, get_version_info

# 5. FOUNDER ALIASES
# High-frequency aliases for "Low Labor" coding.
# 'q' is the industry standard for quick unit-tensor instantiation.
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

# 6. INDUSTRIAL LOGGING INITIALIZATION
import logging
from phystensor.io.logging import logger

# Set a NullHandler by default to prevent "No handler found" warnings 
# in downstream enterprise applications.
logging.getLogger("phystensor").addHandler(logging.NullHandler())

# Print diagnostic banner if in a verbose/dev environment
import os
if os.getenv("PHYSTENSOR_VERBOSE") == "1":
    print(f"--- Phystensor Engine v{__version__} ---")
    print("Industrial SI-Base Logic: Active")
