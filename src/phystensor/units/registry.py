from __future__ import annotations

import operator
import re

import numpy as np
from dataclasses import dataclass

from phystensor.units.dimensions import Dimensions


@dataclass(frozen=True)
class Unit:
    symbol: str
    dimensions: Dimensions
    scale: float = 1.0
    offset: float = 0.0  # Crucial for Temp (Celsius/Fahrenheit)

    def to_base(
        self,
        value: float | np.ndarray,
    ) -> float | np.ndarray:
        return (value * self.scale) + self.offset

    def from_base(
        self,
        value: float | np.ndarray,
    ) -> float | np.ndarray:
        return (value - self.offset) / self.scale


class UniversalRegistry:
    def __init__(self) -> None:
        self._store: dict[str, Unit] = {}
        self._prefixes: dict[str, float] = {
            "Q": 1e30,
            "R": 1e27,
            "Y": 1e24,
            "Z": 1e21,
            "E": 1e18,
            "P": 1e15,
            "T": 1e12,
            "G": 1e9,
            "M": 1e6,
            "k": 1e3,
            "h": 1e2,
            "da": 1e1,
            "d": 1e-1,
            "c": 1e-2,
            "m": 1e-3,
            "u": 1e-6,
            "μ": 1e-6,
            "n": 1e-9,
            "p": 1e-12,
            "f": 1e-15,
            "a": 1e-18,
            "z": 1e-21,
            "y": 1e-24,
        }
        # Pre-populate fundamental identity units
        self.define("m",   Dimensions((1, 0, 0, 0, 0, 0, 0)))  # Length
        self.define("kg",  Dimensions((0, 1, 0, 0, 0, 0, 0)))  # Mass
        self.define("s",   Dimensions((0, 0, 1, 0, 0, 0, 0)))  # Time
        self.define("A",   Dimensions((0, 0, 0, 1, 0, 0, 0)))  # Current
        self.define("K",   Dimensions((0, 0, 0, 0, 1, 0, 0)))  # Temperature
        self.define("mol", Dimensions((0, 0, 0, 0, 0, 1, 0)))  # Amount
        self.define("cd",  Dimensions((0, 0, 0, 0, 0, 0, 1)))  # Intensity

    def define(
        self,
        symbol: str,
        dims: Dimensions,
        scale: float = 1.0,
        offset: float = 0.0,
    ) -> Unit:
        unit = Unit(symbol, dims, scale, offset)
        self._store[symbol] = unit
        return unit

    def _resolve(self, symbol: str) -> Unit:
        """Exact match, empty string, exponent, or metric prefix."""
        if symbol in self._store:
            return self._store[symbol]

        if not symbol or symbol.strip() == "":
            return Unit("", Dimensions((0, 0, 0, 0, 0, 0, 0)), 1.0)

        # Exponent notation: m^2, s^-1
        if "^" in symbol:
            base_str, exp_str = symbol.split("^", 1)
            base = self._resolve(base_str)
            exp = int(exp_str)
            return Unit(
                symbol,
                base.dimensions ** exp,
                base.scale ** exp,
                0.0,
            )

        # Metric prefixes (longest match first)
        for pfx, factor in sorted(
            self._prefixes.items(), key=lambda x: -len(x[0])
        ):
            if symbol.startswith(pfx):
                rest = symbol[len(pfx):]
                if rest in self._store:
                    base = self._store[rest]
                    return Unit(
                        symbol,
                        base.dimensions,
                        base.scale * factor,
                        base.offset,
                    )

        raise KeyError(symbol)

    def _parse_compound(self, expr: str) -> Unit:
        """Handle expressions like kg*m/s^2."""
        tokens = re.split(r"(\*|/)", expr)
        tokens = [t.strip() for t in tokens if t.strip()]

        if not tokens:
            raise KeyError(f"Cannot parse unit expression: {expr}")

        result = self._resolve(tokens[0])
        i = 1
        while i < len(tokens):
            op = tokens[i]
            if op not in ("*", "/"):
                raise KeyError(
                    f"Unexpected token '{op}' in unit expression: {expr}"
                )
            if i + 1 >= len(tokens):
                raise KeyError(
                    f"Trailing operator in unit expression: {expr}"
                )
            nxt = self._resolve(tokens[i + 1])
            if op == "*":
                result = Unit(
                    f"{result.symbol}*{nxt.symbol}",
                    result.dimensions * nxt.dimensions,
                    result.scale * nxt.scale,
                    0.0,
                )
            else:
                result = Unit(
                    f"{result.symbol}/{nxt.symbol}",
                    result.dimensions / nxt.dimensions,
                    result.scale / nxt.scale,
                    0.0,
                )
            i += 2

        return result

    def lookup(self, symbol: str) -> Unit:
        if not isinstance(symbol, str):
            raise TypeError("Unit symbol must be a string")
        try:
            return self._resolve(symbol)
        except KeyError:
            pass

        if "*" in symbol or "/" in symbol:
            return self._parse_compound(symbol)

        raise KeyError(
            f"Unit '{symbol}' not recognized. "
            "Define it via registry.define()."
        )


# Global Instance for the Phystensor Ecosystem
registry = UniversalRegistry()

# Constants based on the 2019 redefinition of SI base units
# Vector format: (L, M, T, I, Θ, N, J)

# --- COSMOLOGICAL & RELATIVISTIC ---
registry.define("c", Dimensions((1, 0, -1, 0, 0, 0, 0)), 299792458.0)
registry.define("G", Dimensions((3, -1, -2, 0, 0, 0, 0)), 6.67430e-11)
registry.define("H0", Dimensions((0, 0, -1, 0, 0, 0, 0)), 2.268e-18)

# --- QUANTUM & ATOMIC ---
registry.define("h", Dimensions((2, 1, -1, 0, 0, 0, 0)), 6.62607015e-34)
registry.define("hbar", Dimensions((2, 1, -1, 0, 0, 0, 0)), 1.054571817e-34)
registry.define("alpha", Dimensions((0, 0, 0, 0, 0, 0, 0)), 7.297352569e-3)

# --- ELECTROMAGNETIC ---
registry.define(
    "e_charge", Dimensions((0, 0, 1, 1, 0, 0, 0)), 1.602176634e-19
)
registry.define(
    "eps0", Dimensions((-3, -1, 4, 2, 0, 0, 0)), 8.8541878128e-12
)
registry.define(
    "mu0", Dimensions((1, 1, -2, -2, 0, 0, 0)), 1.25663706212e-6
)

# --- THERMODYNAMIC & CHEMICAL ---
registry.define(
    "kB", Dimensions((2, 1, -2, 0, -1, 0, 0)), 1.380649e-23
)
registry.define(
    "NA", Dimensions((0, 0, 0, 0, 0, -1, 0)), 6.02214076e23
)
registry.define(
    "R_gas", Dimensions((2, 1, -2, 0, -1, -1, 0)), 8.314462618
)
registry.define(
    "sigma_sb", Dimensions((0, 1, -3, 0, -4, 0, 0)), 5.670374e-8
)

# --- ASTRONOMICAL SCALES ---
registry.define("M_earth", Dimensions((0, 1, 0, 0, 0, 0, 0)), 5.9722e24)
registry.define("R_earth", Dimensions((1, 0, 0, 0, 0, 0, 0)), 6371000.0)
registry.define("M_sun",   Dimensions((0, 1, 0, 0, 0, 0, 0)), 1.98847e30)
registry.define("AU",      Dimensions((1, 0, 0, 0, 0, 0, 0)), 149597870700.0)
registry.define("ly",      Dimensions((1, 0, 0, 0, 0, 0, 0)), 9.46073e15)

# --- DERIVED SI UNITS ---
registry.define("Hz",  Dimensions((0, 0, -1, 0, 0, 0, 0)), 1.0)
registry.define("N",   Dimensions((1, 1, -2, 0, 0, 0, 0)), 1.0)
registry.define("Pa",  Dimensions((-1, 1, -2, 0, 0, 0, 0)), 1.0)
registry.define("J",   Dimensions((2, 1, -2, 0, 0, 0, 0)), 1.0)
registry.define("W",   Dimensions((2, 1, -3, 0, 0, 0, 0)), 1.0)
registry.define("C",   Dimensions((0, 0, 1, 1, 0, 0, 0)), 1.0)
registry.define("V",   Dimensions((2, 1, -3, -1, 0, 0, 0)), 1.0)
registry.define("ohm", Dimensions((2, 1, -3, -2, 0, 0, 0)), 1.0)
registry.define("S",   Dimensions((-2, -1, 3, 2, 0, 0, 0)), 1.0)
registry.define("F",   Dimensions((-2, -1, 4, 2, 0, 0, 0)), 1.0)
registry.define("Wb",  Dimensions((2, 1, -2, -1, 0, 0, 0)), 1.0)
registry.define("T",   Dimensions((0, 1, -2, -1, 0, 0, 0)), 1.0)
registry.define("H",   Dimensions((2, 1, -2, -2, 0, 0, 0)), 1.0)

# --- COMMON NON-SI UNITS ---
registry.define("min", Dimensions((0, 0, 1, 0, 0, 0, 0)), 60.0)
registry.define("hr",  Dimensions((0, 0, 1, 0, 0, 0, 0)), 3600.0)
registry.define("day", Dimensions((0, 0, 1, 0, 0, 0, 0)), 86400.0)
registry.define("yr",  Dimensions((0, 0, 1, 0, 0, 0, 0)), 31557600.0)
registry.define("g",   Dimensions((0, 1, 0, 0, 0, 0, 0)), 0.001)
registry.define("t",   Dimensions((0, 1, 0, 0, 0, 0, 0)), 1000.0)
registry.define("kn",  Dimensions((1, 0, -1, 0, 0, 0, 0)), 0.514444444)
registry.define("degC", Dimensions((0, 0, 0, 0, 1, 0, 0)), 1.0, 273.15)
registry.define("degF", Dimensions((0, 0, 0, 0, 1, 0, 0)), 5.0 / 9.0, 255.372222)


# --- COMMON ALIASES ---
registry.define("meter",     Dimensions((1, 0, 0, 0, 0, 0, 0)), 1.0)
registry.define("femtometer", Dimensions((1, 0, 0, 0, 0, 0, 0)), 1e-15)
