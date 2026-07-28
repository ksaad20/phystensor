import numpy as np
from typing import Any, Union, List
from phystensor.core.tensor import PhysicalTensor
from phystensor.units.registry import registry

class ConversionEngine:
    """
    Handles the movement of data between human-readable units 
    and the high-performance SI-base PhysicalTensor.
    """

    @staticmethod
    def to_tensor(data: Any, unit_symbol: str) -> PhysicalTensor:
        """
        Creates a PhysicalTensor from raw data by normalizing it 
        to SI base using the registry.
        """
        unit = registry.lookup(unit_symbol)
        
        # Convert raw data to SI base values
        # e.g., if data is 10 and unit is 'km', base_data becomes 10000
        base_data = unit.to_base(np.asanyarray(data))
        
        return PhysicalTensor(base_data, unit.dimensions)

    @staticmethod
    def from_tensor(tensor: PhysicalTensor, target_unit_symbol: str) -> np.ndarray:
        """
        Converts an SI-base PhysicalTensor back into a specific unit.
        Verifies dimensional integrity before conversion.
        """
        target_unit = registry.lookup(target_unit_symbol)
        
        if tensor.dimensions != target_unit.dimensions:
            raise TypeError(
                f"Conversion Mismatch: Cannot convert {tensor.dimensions.vector} "
                f"to '{target_unit_symbol}' ({target_unit.dimensions.vector})"
            )
            
        return target_unit.from_base(tensor.data)

    @staticmethod
    def convert_batch(tensors: List[PhysicalTensor], target_unit: str) -> List[np.ndarray]:
        """High-frequency batch conversion for sensor streams or simulation frames."""
        return [ConversionEngine.from_tensor(t, target_unit) for t in tensors]

# Global Factory Alias for "Low Labor" usage
def quantity(value: Any, unit: str) -> PhysicalTensor:
    """The primary entry point for creating unit-aware data."""
    return ConversionEngine.to_tensor(value, unit)
