"""Unit conversion utilities for PhysicalTensor."""

from typing import Any

import numpy as np

from phystensor.core.tensor import PhysicalTensor
from phystensor.units.registry import registry


class ConversionEngine:
    """Convert between user-facing units and SI-base PhysicalTensor objects."""

    @staticmethod
    def to_tensor(data: Any, unit_symbol: str) -> PhysicalTensor:
        """
        Create a PhysicalTensor by converting input data to SI base units.

        Parameters
        ----------
        data
            Numeric scalar or array-like input.
        unit_symbol
            Unit symbol registered in the unit registry.

        Returns
        -------
        PhysicalTensor
            Tensor stored internally in SI base units.
        """
        unit = registry.lookup(unit_symbol)

        base_data = unit.to_base(np.asanyarray(data))

        return PhysicalTensor(base_data, unit.dimensions)

    @staticmethod
    def from_tensor(
        tensor: PhysicalTensor,
        target_unit_symbol: str,
    ) -> np.ndarray:
        """
        Convert an SI-base PhysicalTensor into the requested unit.

        Raises
        ------
        TypeError
            If the tensor dimensions do not match the target unit.
        """
        target_unit = registry.lookup(target_unit_symbol)

        if tensor.dimensions != target_unit.dimensions:
            raise TypeError(
                "Conversion mismatch: cannot convert "
                f"{tensor.dimensions.vector} "
                f"to '{target_unit_symbol}' "
                f"({target_unit.dimensions.vector})."
            )

        return target_unit.from_base(tensor.data)

    @staticmethod
    def convert_batch(
        tensors: list[PhysicalTensor],
        target_unit: str,
    ) -> list[np.ndarray]:
        """
        Convert multiple tensors into the same target unit.

        Parameters
        ----------
        tensors
            List of PhysicalTensor objects.
        target_unit
            Target unit symbol.

        Returns
        -------
        list[np.ndarray]
            Converted values.
        """
        return [
            ConversionEngine.from_tensor(tensor, target_unit)
            for tensor in tensors
        ]


def quantity(value: Any, unit: str) -> PhysicalTensor:
    """
    Create a PhysicalTensor from a numeric value and unit.

    This is the primary public factory function.
    """
    return ConversionEngine.to_tensor(value, unit)
