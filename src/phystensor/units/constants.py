from phystensor.core.tensor import PhysicalTensor
from phystensor.units.dimensions import Dimensions
from phystensor.utils.math_const import PI

# --- FUNDAMENTAL CONSTANTS (CODATA 2026 Standards) ---

# Speed of Light in Vacuum [L T^-1]
c = PhysicalTensor(299792458.0, Dimensions((1, 0, -1, 0, 0, 0, 0)))

# Gravitational Constant [L^3 M^-1 T^-2]
G = PhysicalTensor(6.67430e-11, Dimensions((3, -1, -2, 0, 0, 0, 0)))

# Planck Constant [L^2 M T^-1]
h = PhysicalTensor(6.62607015e-34, Dimensions((2, 1, -1, 0, 0, 0, 0)))
hbar = PhysicalTensor(6.62607015e-34 / (2 * PI), Dimensions((2, 1, -1, 0, 0, 0, 0)))

# Elementary Charge [T I]
e = PhysicalTensor(1.602176634e-19, Dimensions((0, 0, 1, 1, 0, 0, 0)))

# Boltzmann Constant [L^2 M T^-2 Theta^-1]
k_B = PhysicalTensor(1.380649e-23, Dimensions((2, 1, -2, 0, -1, 0, 0)))

# Avogadro Constant [N^-1]
N_A = PhysicalTensor(6.02214076e23, Dimensions((0, 0, 0, 0, 0, -1, 0)))

# --- ELECTROMAGNETIC CONSTANTS (EEE Engineering) ---

# Vacuum Permittivity (epsilon_0) [L^-3 M^-1 T^4 I^2]
eps_0 = PhysicalTensor(8.8541878128e-12, Dimensions((-3, -1, 4, 2, 0, 0, 0)))

# Vacuum Permeability (mu_0) [L M T^-2 I^-2]
mu_0 = PhysicalTensor(1.25663706212e-6, Dimensions((1, 1, -2, -2, 0, 0, 0)))

# Impedance of Free Space (~377 ohms)
Z_0 = PhysicalTensor(376.730313668, Dimensions((2, 1, -3, -2, 0, 0, 0)))

# --- ASTROPHYSICAL & GEOPHYSICAL ---

# Standard Gravity (Earth) [L T^-2]
g_n = PhysicalTensor(9.80665, Dimensions((1, 0, -2, 0, 0, 0, 0)))

# Solar Mass [M]
M_sun = PhysicalTensor(1.98847e30, Dimensions((0, 1, 0, 0, 0, 0, 0)))

# Astronomical Unit [L]
AU = PhysicalTensor(149597870700.0, Dimensions((1, 0, 0, 0, 0, 0, 0)))

# --- NUCLEAR & ATOMIC ---

# Electron Rest Mass [M]
m_e = PhysicalTensor(9.1093837e-31, Dimensions((0, 1, 0, 0, 0, 0, 0)))

# Proton Rest Mass [M]
m_p = PhysicalTensor(1.6726219e-27, Dimensions((0, 1, 0, 0, 0, 0, 0)))

# Stefan-Boltzmann Constant [M T^-3 Theta^-4]
sigma_sb = PhysicalTensor(5.670374419e-8, Dimensions((0, 1, -3, 0, -4, 0, 0)))
