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

# Constants based on the 2019 redefinition of SI base units
# Vector format: (L, M, T, I, Θ, N, J)

# --- COSMOLOGICAL & RELATIVISTIC ---
# Speed of Light (c): The speed limit of the universe
registry.define("c", Dimensions((1, 0, -1, 0, 0, 0, 0)), 299792458.0)

# Gravitational Constant (G): Governing General Relativity
registry.define("G", Dimensions((3, -1, -2, 0, 0, 0, 0)), 6.67430e-11)

# Hubble Constant (H0): The expansion rate of the universe
registry.define("H0", Dimensions((0, 0, -1, 0, 0, 0, 0)), 2.268e-18)

# --- QUANTUM & ATOMIC ---
# Planck Constant (h): The scale of the subatomic world
registry.define("h", Dimensions((2, 1, -1, 0, 0, 0, 0)), 6.62607015e-34)

# Reduced Planck Constant (hbar)
registry.define("hbar", Dimensions((2, 1, -1, 0, 0, 0, 0)), 1.054571817e-34)

# Fine-structure constant (alpha): Dimensionless (0,0,0,0,0,0,0)
registry.define("alpha", Dimensions((0, 0, 0, 0, 0, 0, 0)), 7.297352569e-3)

# --- ELECTROMAGNETIC (EEE Core) ---
# Elementary Charge (e): The charge of a single electron
registry.define("e_charge", Dimensions((0, 0, 1, 1, 0, 0, 0)), 1.602176634e-19)

# Vacuum Permittivity (epsilon_0)
registry.define("eps0", Dimensions((-3, -1, 4, 2, 0, 0, 0)), 8.8541878128e-12)

# Vacuum Permeability (mu_0)
registry.define("mu0", Dimensions((1, 1, -2, -2, 0, 0, 0)), 1.25663706212e-6)

# --- THERMODYNAMIC & CHEMICAL ---
# Boltzmann Constant (k_B): Bridging Temp and Energy
registry.define("kB", Dimensions((2, 1, -2, 0, -1, 0, 0)), 1.380649e-23)

# Avogadro Constant (N_A): The link to the macroscopic world
registry.define("NA", Dimensions((0, 0, 0, 0, 0, -1, 0)), 6.02214076e23)

# Molar Gas Constant (R)
registry.define("R_gas", Dimensions((2, 1, -2, 0, -1, -1, 0)), 8.314462618)

# Stefan-Boltzmann Constant (sigma)
registry.define("sigma_sb", Dimensions((0, 1, -3, 0, -4, 0, 0)), 5.670374e-8)

# --- ASTRONOMICAL SCALES ---
registry.define("M_earth", Dimensions((0, 1, 0, 0, 0, 0, 0)), 5.9722e24)
registry.define("R_earth", Dimensions((1, 0, 0, 0, 0, 0, 0)), 6371000.0)
registry.define("M_sun",   Dimensions((0, 1, 0, 0, 0, 0, 0)), 1.98847e30)
registry.define("AU",      Dimensions((1, 0, 0, 0, 0, 0, 0)), 149597870700.0)
