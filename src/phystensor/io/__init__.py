"""
The I/O and Lifecycle Module for phystensor.
Handles conversion, logging, schema validation, and package metadata.
"""

# Initialize structured logging on module load
import logging
logging.getLogger("phystensor").addHandler(logging.NullHandler())
