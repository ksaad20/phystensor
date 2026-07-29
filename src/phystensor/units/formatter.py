from typing import Dict, List, Tuple
from phystensor.units.dimensions import Dimensions
from phystensor.units.definitions import UNIT_DEFINITIONS

class PhysicsFormatter:
    """
    The 'Human Interface' of the engine. 
    Converts internal SI-vectors into professional engineering notation.
    """

    # SI Base Symbols for raw vector formatting
    BASE_SYMBOLS: List[str] = ["m", "kg", "s", "A", "K", "mol", "cd"]

    @classmethod
    def to_unit_string(cls, dims: Dimensions, preferred_unit: str = None) -> str:
        """
        Translates a Dimensions object into a readable string.
        Logic:
        1. Checks if the vector matches a named derived unit (e.g., 'V' for Volts).
        2. If no match, constructs a raw SI string (e.g., 'kg*m/s^2').
        """
        # 1. Check for a direct match in UNIT_DEFINITIONS
        if not preferred_unit:
            for symbol, data in UNIT_DEFINITIONS.items():
                if data["dim"] == dims.vector and data["scale"] == 1.0:
                    return symbol
        
        # 2. Build the string from base components
        pos_terms: List[str] = []
        neg_terms: List[str] = []

        for i, exponent in enumerate(dims.vector):
            if exponent == 0:
                continue
            
            symbol = cls.BASE_SYMBOLS[i]
            term = f"{symbol}^{exponent}" if exponent != 1 and exponent != -1 else symbol
            
            if exponent > 0:
                pos_terms.append(term)
            else:
                # Remove negative sign for denominator formatting
                neg_terms.append(term.replace("-", ""))

        # 3. Assemble components
        numerator = " * ".join(pos_terms) if pos_terms else "1"
        if not neg_terms:
            return numerator
        
        denominator = " * ".join(neg_terms)
        return f"{numerator} / ({denominator})" if len(neg_terms) > 1 else f"{numerator} / {denominator}"

    @staticmethod
    def format_value(value: float, precision: int = 4) -> str:
        """Formats the numerical component for industrial clarity (Scientific vs Standard)."""
        if abs(value) >= 1e6 or (abs(value) <= 1e-4 and value != 0):
            return f"{value:.{precision}e}"
        return f"{value:.{precision}f}"

    @classmethod
    def pretty_print(cls, tensor_data: any, dims: Dimensions) -> str:
        """The standard __repr__ output for a PhysicalTensor."""
        unit_str = cls.to_unit_string(dims)
        # Handle scalar vs array data
        val_str = cls.format_value(tensor_data) if hasattr(tensor_data, "__float__") else str(tensor_data)
        return f"{val_str} [{unit_str}]"

class ANSIColorFormatter:
    """Optional utility for terminal-based color coding of dimensions."""
    
    COLORS = {
        "Length": "\033[94m",  # Blue
        "Mass": "\033[92m",    # Green
        "Time": "\033[93m",    # Yellow
        "Current": "\033[91m", # Red
        "RESET": "\033[0m"
    }

    @staticmethod
    def highlight(unit_str: str) -> str:
        # Simple color-coding for high-visibility debugging
                return (
            f"{ANSIColorFormatter.COLORS['Length']}"
            f"{unit_str}"
            f"{ANSIColorFormatter.COLORS['RESET']}"
                )
