"""
The I/O and Lifecycle Module for phystensor.
Handles conversion, logging, schema validation, and package metadata.
"""

from phystensor.io.conversion import ConversionEngine, quantity
from phystensor.io.logging import logger, log_dimension_error
from phystensor.io.version import __version__, get_version_info
from phystensor.io.json import save_json, load_json
from phystensor.io.typing import TensorLike, SIVector

__all__ = [
    "ConversionEngine",
    "quantity",
    "logger",
    "log_dimension_error",
    "__version__",
    "get_version_info",
    "save_json",
    "load_json",
    "TensorLike",
    "SIVector",
]

# Initialize structured logging on module load
import logging
logging.getLogger("phystensor").addHandler(logging.NullHandler())
