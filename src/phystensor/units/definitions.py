from typing import Dict, Any, Final
from phystensor.units.dimensions import Dimensions

# The SI 7-Vector: [L, M, T, I, Θ, N, J]
UNIT_DEFINITIONS: Final[Dict[str, Dict[str, Any]]] = {
    # --- BASE SI ---
    "m":   {"dim": (1, 0, 0, 0, 0, 0, 0), "scale": 1.0},
    "kg":  {"dim": (0, 1, 0, 0, 0, 0, 0), "scale": 1.0},
    "s":   {"dim": (0, 0, 1, 0, 0, 0, 0), "scale": 1.0},
    "A":   {"dim": (0, 0, 0, 1, 0, 0, 0), "scale": 1.0},
    "K":   {"dim": (0, 0, 0, 0, 1, 0, 0), "scale": 1.0},
    "mol": {"dim": (0, 0, 0, 0, 0, 1, 0), "scale": 1.0},
    "cd":  {"dim": (0, 0, 0, 0, 0, 0, 1), "scale": 1.0},

    # --- AEROSPACE & NAVAL ARCHITECTURE (Added: Slugs, knots, buoyancy) ---
    "slug": {"dim": (0, 1, 0, 0, 0, 0, 0), "scale": 14.5939}, # Imperial mass
    "lbf":  {"dim": (1, 1, -2, 0, 0, 0, 0), "scale": 4.44822},
    "kn":   {"dim": (1, 0, -1, 0, 0, 0, 0), "scale": 0.51444},
    "nmi":  {"dim": (1, 0, 0, 0, 0, 0, 0), "scale": 1852.0},
    "stokes": {"dim": (2, 0, -1, 0, 0, 0, 0), "scale": 1e-4}, # Kinematic Viscosity

    # --- CIVIL, HYDRAULIC & GEOTECHNICAL (Added: Darcy, Poise) ---
    "psi":   {"dim": (-1, 1, -2, 0, 0, 0, 0), "scale": 6894.76},
    "darcy": {"dim": (2, 0, 0, 0, 0, 0, 0), "scale": 9.869233e-13}, # Permeability
    "poise": {"dim": (-1, 1, -1, 0, 0, 0, 0), "scale": 0.1}, # Dynamic Viscosity
    "cfs":   {"dim": (3, 0, -1, 0, 0, 0, 0), "scale": 0.0283168}, # Cubic feet per sec
    "acre_ft": {"dim": (3, 0, 0, 0, 0, 0, 0), "scale": 1233.48}, # Reservoir volume

    # --- EEE & SEMICONDUCTOR (Added: Maxwell, Mho, Gilbert) ---
    "V":      {"dim": (2, 1, -3, -1, 0, 0, 0), "scale": 1.0},
    "ohm":    {"dim": (2, 1, -3, -2, 0, 0, 0), "scale": 1.0},
    "mho":    {"dim": (-2, -1, 3, 2, 0, 0, 0), "scale": 1.0}, # Conductance (S)
    "maxwell": {"dim": (2, 1, -2, -1, 0, 0, 0), "scale": 1e-8}, # Magnetic flux
    "gilbert": {"dim": (0, 0, 0, 1, 0, 0, 0), "scale": 0.79577}, # MMF
    "oersted": {"dim": (-1, 0, 0, 1, 0, 0, 0), "scale": 79.577}, # Magnetic intensity

    # --- MECHATRONICS & CONTROL (Added: Jiffies, Ticks) ---
    "rpm":  {"dim": (0, 0, -1, 0, 0, 0, 0), "scale": 0.1047198},
    "oz_in": {"dim": (2, 1, -2, 0, 0, 0, 0), "scale": 0.00706155}, # Motor torque
    "rad_s2": {"dim": (0, 0, -2, 0, 0, 0, 0), "scale": 1.0}, # Ang. acceleration

    # --- BIOMEDICAL & RADIOLOGY (Added: Curie, Becquerel, Roentgen) ---
    "mmHg": {"dim": (-1, 1, -2, 0, 0, 0, 0), "scale": 133.322},
    "Bq":   {"dim": (0, 0, -1, 0, 0, 0, 0), "scale": 1.0}, # Radioactivity
    "Ci":   {"dim": (0, 0, -1, 0, 0, 0, 0), "scale": 3.7e10}, # Curie
    "R":    {"dim": (-1, 0, 1, 1, 0, 0, 0), "scale": 0.000258}, # Roentgen (C/kg air)

    # --- ASTROPHYSICS & COSMOLOGY (Added: Jansky, Solar Luminosity) ---
    "Jy":    {"dim": (0, 1, -2, 0, 0, 0, 0), "scale": 1e-26}, # Flux density
    "L_sun": {"dim": (2, 1, -3, 0, 0, 0, 0), "scale": 3.828e26}, # Solar Lum
    "R_sun": {"dim": (1, 0, 0, 0, 0, 0, 0), "scale": 6.957e8}, # Solar Radius

    # --- CSE & DATA PHYSICS (Added: Erlang, Shannons) ---
    "bit":  {"dim": (0, 0, 0, 0, 0, 0, 0), "scale": 1.0},
    "byte": {"dim": (0, 0, 0, 0, 0, 0, 0), "scale": 8.0},
    "shannon": {"dim": (0, 0, 0, 0, 0, 0, 0), "scale": 1.0}, # Unit of info
    "erlang":  {"dim": (0, 0, 0, 0, 0, 0, 0), "scale": 1.0}, # Telephony traffic

    # --- NUCLEAR & QUANTUM (Added: Fermi, Hartree) ---
    "eV":      {"dim": (2, 1, -2, 0, 0, 0, 0), "scale": 1.60218e-19},
    "femtometer": {"dim": (1, 0, 0, 0, 0, 0, 0), "scale": 1e-15}, # "Fermi"
    "hartree": {"dim": (2, 1, -2, 0, 0, 0, 0), "scale": 4.35974e-18}, # Atomic energy
}
