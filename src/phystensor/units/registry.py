from dataclasses import dataclass, field
from typing import Dict, Optional
from phystensor.units.dimensions import Dimensions

@dataclass(frozen=True)
class Unit:
    symbol: str
    dimensions: Dimensions
    scale_factor: float = 1.0  # Multiplier to reach SI base unit
    offset: float = 0.0        # For non-linear scales like Celsius/Fahrenheit

    def to_base(self, value: float) -> float:
        return (value * self.scale_factor) + self.offset

    def from_base(self, value: float) -> float:
        return (value - self.offset) / self.scale_factor

class Registry:
    """
    A universal lookup for any unit defined in any branch of physics.
    Designed for 100% interoperability.
    """
    def __init__(self):
        self._units: Dict[str, Unit] = {}

    def define(self, symbol: str, dims: Dimensions, scale: float = 1.0, offset: float = 0.0):
        unit = Unit(symbol, dims, scale, offset)
        self._units[symbol] = unit
        return unit

    def get(self, symbol: str) -> Unit:
        if symbol not in self._units:
            raise ValueError(f"Unit '{symbol}' is not defined in the universal registry.")
        return self._units[symbol]

# Initialize the Global Universal Registry
U = Registry()
