from dataclasses import dataclass
from typing import Tuple

# The 7 SI Base Dimensions (The Order is Immutable)
# 0: Length (L) - meter
# 1: Mass (M) - kilogram
# 2: Time (T) - second
# 3: Electric Current (I) - ampere
# 4: Thermodynamic Temperature (Θ) - kelvin
# 5: Amount of Substance (N) - mole
# 6: Luminous Intensity (J) - candela

@dataclass(frozen=True)
class Dimensions:
    """
    The fundamental representation of physical dimensions.
    Exponents are stored as a tuple of 7 integers/fractions.
    """
    vector: Tuple[int, ...] = (0, 0, 0, 0, 0, 0, 0)

    def __add__(self, other):
        # Adding dimensions = Multiplying units (e.g., L * L = L^2)
        return Dimensions(tuple(a + b for a, b in zip(self.vector, other.vector)))

    def __sub__(self, other):
        # Subtracting dimensions = Dividing units (e.g., L / T = L^1 T^-1)
        return Dimensions(tuple(a - b for a, b in zip(self.vector, other.vector)))
