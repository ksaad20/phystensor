"""
Linear algebra module metadata.

Provides version information and backend details for the
PhysTensor linear algebra subsystem.
"""

from __future__ import annotations

from typing import Final


__linalg_version__: Final[str] = "1.0.0"
__backend__: Final[str] = "numpy.linalg"


def get_linalg_metadata() -> dict[str, str]:
    """
    Return metadata describing the linear algebra backend.

    Returns
    -------
    dict[str, str]
        Metadata containing:
        - module version
        - computational backend
        - numerical precision

    Examples
    --------
    >>> get_linalg_metadata()
    {
        "version": "1.0.0",
        "backend": "numpy.linalg",
        "precision": "double"
    }
    """
    return {
        "version": __linalg_version__,
        "backend": __backend__,
        "precision": "double",
    }


__all__ = [
    "__linalg_version__",
    "__backend__",
    "get_linalg_metadata",
]
