from __future__ import annotations

from typing import Any

from phystensor.io.logging import log_dimension_error
from phystensor.units.dimensions import Dimensions


class PhysicsValidationError(Exception):
    """Custom exception for non-physical operations."""


class DimensionalityManager:
    """
    The guardian of physical laws.
    Checks for dimensionless requirements and consistency.
    """

    @staticmethod
    def is_dimensionless(dims: Dimensions) -> bool:
        """Check if all exponents in the SI vector are zero."""
        return all(exponent == 0 for exponent in dims.vector)

    @classmethod
    def validate_transcendental(
        cls, dims: Dimensions, func_name: str
    ) -> None:
        """
        Validate functions like sin, cos, tan, log, exp.

        In physics, you cannot take the log of '5 meters'.
        The input must be a ratio (dimensionless).
        """
        if not cls.is_dimensionless(dims):
            raise PhysicsValidationError(
                "Invalid Physical Operation: '"
                + func_name
                + "' requires a dimensionless input. "
                "Received dimensions: "
                + str(dims.vector)
                + "."
            )

    @classmethod
    def validate_addition(
        cls, dims_a: Dimensions, dims_b: Dimensions
    ) -> None:
        """Ensure apples are not added to oranges."""
        if dims_a != dims_b:
            log_dimension_error(
                PhysicsValidationError("Mismatch"), dims_a, dims_b
            )
            raise PhysicsValidationError(
                "Dimensional Mismatch: Cannot add/subtract quantities "
                "with different dimensions. LHS: "
                + str(dims_a.vector)
                + " vs RHS: "
                + str(dims_b.vector)
                + "."
            )

    @classmethod
    def validate_power(cls, exponent: Any) -> None:
        """
        Ensure exponents are scalars.

        You can have x^2, but you cannot have x^(2 meters).
        """
        from phystensor.core.tensor import PhysicalTensor

        if isinstance(exponent, PhysicalTensor):
            if not cls.is_dimensionless(exponent.dimensions):
                raise PhysicsValidationError(
                    "Exponents must be dimensionless scalars or arrays."
                )


def guard_transcendental(func):
    """
    A decorator to wrap mathematical functions, enforcing
    dimensionless inputs automatically.
    """

    def wrapper(tensor, *args, **kwargs):
        DimensionalityManager.validate_transcendental(
            tensor.dimensions, func.__name__
        )
        return func(tensor, *args, **kwargs)

    return wrapper
