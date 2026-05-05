"""
phystensor version metadata.
Format: MAJOR.MINOR.PATCH
"""

__version__ = "1.0.0"

def get_version_info() -> str:
    """Returns a detailed version string for industrial logging."""
    return f"Phystensor v{__version__} - Xylema Industrial Physics Engine"
