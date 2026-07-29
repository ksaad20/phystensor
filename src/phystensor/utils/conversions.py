from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from phystensor.core.tensor import PhysicalTensor

from phystensor.core.tensor import PhysicalTensor
from phystensor.units.registry import registry


class TensorConverter:
    """
    High-level utility for scaling and transforming PhysicalTensors
    between compatible units within the system.
    """

    @staticmethod
    def scale_to(tensor: PhysicalTensor, target_unit_symbol: str) -> PhysicalTensor:
        """
        Returns a NEW PhysicalTensor scaled to a target unit.
        Example: Convert a tensor in 'meters' to 'kilometers'.
        """
        target_unit = registry.lookup(target_unit_symbol)

        if tensor.dimensions != target_unit.dimensions:
            raise TypeError(
                f"Incompatible Dimensions: {tensor.dimensions} vs {target_unit_symbol}"
            )

        # Scale data: (Data in Base SI) / (Target Unit Scale)
        new_data = target_unit.from_base(tensor.data)
        return PhysicalTensor(new_data, tensor.dimensions)

    @staticmethod
    def to_dimensionless(tensor: PhysicalTensor) -> float:
        """Force-extracts the raw value of a dimensionless tensor."""
        if not all(v == 0 for v in tensor.dimensions.vector):
            raise ValueError("Cannot extract raw value from a unit-carrying tensor.")
        return tensor.data
