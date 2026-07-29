from typing import Dict, Final

# Metric (SI) Prefixes: Defined as multipliers relative to the base unit.
# These follow the international standard (BIPM).

PREFIXES: Final[dict[str, float]] = {
    # Large Scales (Macro/Cosmic)
    "Q": 1e30,   # quetta
    "R": 1e27,   # ronna
    "Y": 1e24,   # yotta
    "Z": 1e21,   # zetta
    "E": 1e18,   # exa
    "P": 1e15,   # peta
    "T": 1e12,   # tera
    "G": 1e9,    # giga
    "M": 1e6,    # mega
    "k": 1e3,    # kilo
    "h": 100.0,  # hecto
    "da": 10.0,  # deca
    
    # Base (Unity)
    "": 1.0,     # No prefix
    
    # Small Scales (Micro/Quantum)
    "d": 0.1,    # deci
    "c": 0.01,   # centi
    "m": 1e-3,   # milli
    "u": 1e-6,   # micro (using 'u' for ASCII compatibility in APIs)
    "n": 1e-9,   # nano
    "p": 1e-12,  # pico
    "f": 1e-15,  # femto
    "a": 1e-18,  # atto
    "z": 1e-21,  # zepto
    "y": 1e-24,  # yocto
    "r": 1e-27,  # ronto
    "q": 1e-30,  # quecto
}

# Binary Prefixes: Critical for Technologist-level computing and data-rate physics.
# These are used for memory-intensive maritime data processing (MiB, GiB).

BINARY_PREFIXES: Final[dict[str, float]] = {
    "Ki": 1024.0,
    "Mi": 1024.0**2,
    "Gi": 1024.0**3,
    "Ti": 1024.0**4,
    "Pi": 1024.0**5,
    "Ei": 1024.0**6,
    "Zi": 1024.0**7,
    "Yi": 1024.0**8,
}

def get_prefix_multiplier(symbol: str) -> float:
    """
    Returns the multiplier for a given prefix symbol.
    Defaults to 1.0 if the prefix is unknown.
    """
    return PREFIXES.get(symbol, BINARY_PREFIXES.get(symbol, 1.0))

def split_unit_string(unit_str: str) -> tuple[str, str]:
    """
    Utility to separate a prefix from a base unit.
    Example: 'km' -> ('k', 'm'), 'MiB' -> ('Mi', 'B')
    """
    # Check binary prefixes first (e.g., 'MiB')
    for p in BINARY_PREFIXES:
        if unit_str.startswith(p):
            return p, unit_str[len(p):]
            
    # Check deca (special 2-letter case)
    if unit_str.startswith("da") and len(unit_str) > 2:
        return "da", unit_str[2:]
        
    # Check standard SI prefixes
    for p in PREFIXES:
        if p and unit_str.startswith(p) and len(unit_str) > len(p):
            return p, unit_str[len(p):]
            
    return "", unit_str
