__linalg_version__ = "1.0.0"
__backend__ = "numpy.linalg"

def get_linalg_metadata() -> dict:
    """Reports the computational backend for the linalg module."""
    return {
        "version": __linalg_version__,
        "backend": __backend__,
        "precision": "double"
    }
