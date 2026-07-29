from __future__ import annotations

import logging
import os

from phystensor import core
from phystensor import io
from phystensor import linalg
from phystensor import utils
from phystensor.core.tensor import PhysicalTensor
from phystensor.io.conversion import quantity
from phystensor.io.logging import logger
from phystensor.io.version import __version__, get_version_info
from phystensor.units.constants import (
    AU,
    G,
    M_sun,
    N_A,
    c,
    e,
    eps_0,
    g_n,
    h,
    k_b,
    mu_0,
    Z_0,
)
from phystensor.utils.math_const import E, PI, TAU

from . import registry


# 1. THE CORE IDENTITY
# Expose the primary class and the factory function for rapid development.
tensor = PhysicalTensor
q = quantity

# 2. THE NAMESPACE BRIDGE
# Allow users to access sub-modules directly (e.g., pt.linalg.solve).

# 3. GLOBAL ENGINEERING CONSTANTS
# Direct access to the physics and math required for immediate calculation.

# 4. SYSTEM METADATA

# 5. FOUNDER ALIASES
# High-frequency aliases for "Low Labor" coding.
# 'q' is the industry standard for quick unit-tensor instantiation.

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
    "c",
    "G",
    "h",
    "e",
    "k_b",
    "N_A",
    "eps_0",
    "mu_0",
    "Z_0",
    "g_n",
    "M_sun",
    "AU",
    "PI",
    "TAU",
    "E",
    "__version__",
    "get_version_info",
]

# 6. INDUSTRIAL LOGGING INITIALIZATION
# Set a NullHandler by default to prevent "No handler found" warnings
# in downstream enterprise applications.
logging.getLogger("phystensor").addHandler(logging.NullHandler())

# Print diagnostic banner if in a verbose/dev environment
if os.getenv("PHYSTENSOR_VERBOSE") == "1":
    print("--- Phystensor Engine v" + __version__ + " ---")
    print("Industrial SI-Base Logic: Active")
