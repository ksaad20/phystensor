import numpy as np
from dataclasses import dataclass
from typing import Dict, Union, Tuple
from phystensor.units.dimensions import Dimensions

@dataclass(frozen=True)
class Unit:
    symbol: str
    dimensions: Dimensions
    scale: float = 1.0
    offset: float = 0.0  # Crucial for Temp (Celsius/Fahrenheit)

    def to_base(self, value: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        return (value * self.scale) + self.offset

    def from_base(self, value: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        return (value - self.offset) / self.scale

class UniversalRegistry:
    def __init__(self):
        self._store: Dict[str, Unit] = {}
        # Pre-populate fundamental identity units
        self.define("m",   Dimensions((1,0,0,0,0,0,0))) # Length
        self.define("kg",  Dimensions((0,1,0,0,0,0,0))) # Mass
        self.define("s",   Dimensions((0,0,1,0,0,0,0))) # Time
        self.define("A",   Dimensions((0,0,0,1,0,0,0))) # Current
        self.define("K",   Dimensions((0,0,0,0,1,0,0))) # Temperature
        self.define("mol", Dimensions((0,0,0,0,0,1,0))) # Amount
        self.define("cd",  Dimensions((0,0,0,0,0,0,1))) # Intensity

    def define(self, symbol: str, dims: Dimensions, scale: float = 1.0, offset: float = 0.0) -> Unit:
        unit = Unit(symbol, dims, scale, offset)
        self._store[symbol] = unit
        return unit

    def lookup(self, symbol: str) -> Unit:
        if symbol not in self._store:
            raise KeyError(f"Unit '{symbol}' not recognized. Define it via registry.define().")
        return self._store[symbol]

# Global Instance for the Phystensor Ecosystem
registry = UniversalRegistry()
