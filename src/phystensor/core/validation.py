import numpy as np
from typing import NoReturn
from phystensor.units.dimensions import Dimensions

class PhysicsValidationError(Exception):
    """Custom exception for non-physical operations."""
    pass

class DimensionalityManager:
    """
    The guardian of physical laws. 
    Checks for dimensionless requirements and consistency.
    """
    
    @staticmethod
    def is_dimensionless(dims: Dimensions) -> bool:
        """Checks if all exponents in the SI vector are zero."""
        return all(exponent == 0 for exponent in dims.vector)

    @classmethod
    def validate_transcendental(cls, dims: Dimensions, func_name: str) -> None:
        """
        Validates functions like sin, cos, tan, log, exp.
        In physics, you cannot take the log of '5 meters'. 
        The input must be a ratio (dimensionless).
        """
        if not cls.is_dimensionless(dims):
            raise PhysicsValidationError(
                f"Invalid Physical Operation: '{func_name}' requires a dimensionless input. "
                f"Received dimensions: {dims.vector}."
            )

    @classmethod
    def validate_addition(cls, dims_a: Dimensions, dims_b: Dimensions) -> None:
        """Ensures apples are not added to oranges."""
        if dims_a != dims_b:
            raise PhysicsValidationError(
                f"Dimensional Mismatch: Cannot add/subtract quantities with different dimensions. "
                f"LHS: {dims_a.vector} vs RHS: {dims_b.vector}."
            )

    @classmethod
    def validate_power(cls, exponent: any) -> None:
        """
        Ensures exponents are scalars. 
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
        DimensionalityManager.validate_transcendental(tensor.dimensions, func.__name__)
        return func(tensor, *args, **kwargs)
    return wrapper

from phystensor.io.logging import log_dimension_error

# Inside a check:
if dims_a != dims_b:
    log_dimension_error(TypeError("Mismatch"), dims_a, dims_b)
    raise TypeError("...")
