import re
from typing import Dict
from phystensor.units.dimensions import Dimensions
from phystensor.units.registry import registry

class DimParser:
    """
    Parses string representations of units into Dimension objects.
    Supports complex expressions like 'kg*m/s^2' or 'W/(m*K)'.
    """
    
    @staticmethod
    def parse_expression(expression: str) -> Dimensions:
        """
        Regex-based parser to decompose unit strings.
        Logic: 
        1. Split by '/' to separate numerator and denominator.
        2. Extract unit symbols and exponents (e.g., 'm^2').
        3. Combine vectors from the registry.
        """
        if not expression or expression == "dimensionless":
            return Dimensions((0, 0, 0, 0, 0, 0, 0))

        parts = expression.split('/')
        numerator = parts[0].strip('() ').split('*')
        denominator = parts[1].strip('() ').split('*') if len(parts) > 1 else []

        final_dim = Dimensions((0, 0, 0, 0, 0, 0, 0))

        for item in numerator:
            if item:
                unit_sym, exp = DimParser._extract_unit_and_power(item)
                unit_dim = registry.lookup(unit_sym).dimensions
                final_dim += (unit_dim * exp)

        for item in denominator:
            if item:
                unit_sym, exp = DimParser._extract_unit_and_power(item)
                unit_dim = registry.lookup(unit_sym).dimensions
                final_dim -= (unit_dim * exp)

        return final_dim

    @staticmethod
    def _extract_unit_and_power(item: str) -> tuple[str, float]:
        item = item.strip()
        if '^' in item:
            parts = item.split('^')
            return parts[0], float(parts[1])
        return item, 1.0
