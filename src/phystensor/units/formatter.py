from __future__ import annotations

from typing import Any

from phystensor.units.dimensions import Dimensions
from phystensor.units.definitions import UNIT_DEFINITIONS


class PhysicsFormatter:
    """
    The 'Human Interface' of the engine.
    Converts internal SI-vectors into professional engineering notation.
    """

    # SI Base Symbols for raw vector formatting
    BASE_SYMBOLS: list[str] = ["m", "kg", "s", "A", "K", "mol", "cd"]

    @classmethod
    def to_unit_string(
        cls, dims: Dimensions, preferred_unit: str | None = None
    ) -> str:
        """
        Translates a Dimensions object into a readable string.

        Logic:
        1. Checks if the vector matches a named derived unit (e.g., 'V').
        2. If no match, constructs a raw SI string (e.g., 'kg*m/s^2').
        """
        # 1. Check for a direct match in UNIT_DEFINITIONS
        if not preferred_unit:
            for symbol, data in UNIT_DEFINITIONS.items():
                if data["dim"] == dims.vector and data["scale"] == 1.0:
                    return symbol

        # 2. Build the string from base components
        pos_terms: list[str] = []
        neg_terms: list[str] = []

        for i, exponent in enumerate(dims.vector):
            if exponent == 0:
                continue

            symbol = cls.BASE_SYMBOLS[i]
            abs_exp = abs(exponent)
            if abs_exp != 1:
                term = symbol + "^" + str(abs_exp)
            else:
                term = symbol

            if exponent > 0:
                pos_terms.append(term)
            else:
                neg_terms.append(term)

        # 3. Assemble components
        numerator = " * ".join(pos_terms) if pos_terms else "1"
        if not neg_terms:
            return numerator

        denominator = " * ".join(neg_terms)
        if len(neg_terms) > 1:
            return numerator + " / (" + denominator + ")"
        return numerator + " / " + denominator

    @staticmethod
    def format_value(value: float, precision: int = 4) -> str:
        """Format numerical component for industrial clarity."""
        if abs(value) >= 1e6 or (abs(value) <= 1e-4 and value != 0):
            return format(value, "." + str(precision) + "e")
        return format(value, "." + str(precision) + "f")

    @classmethod
    def pretty_print(cls, tensor_data: Any, dims: Dimensions) -> str:
        """The standard __repr__ output for a PhysicalTensor."""
        unit_str = cls.to_unit_string(dims)
        if hasattr(tensor_data, "__float__"):
            val_str = cls.format_value(tensor_data)
        else:
            val_str = str(tensor_data)
        return val_str + " [" + unit_str + "]"


class ANSIColorFormatter:
    """Optional utility for terminal-based color coding of dimensions."""

    COLORS = {
        "Length": "\033[94m",  # Blue
        "Mass": "\033[92m",    # Green
        "Time": "\033[93m",    # Yellow
        "Current": "\033[91m",  # Red
        "RESET": "\033[0m",
    }

    @staticmethod
    def highlight(unit_str: str) -> str:
        """Simple color-coding for high-visibility debugging."""
        return (
            ANSIColorFormatter.COLORS["Length"]
            + unit_str
            + ANSIColorFormatter.COLORS["RESET"]
        )
