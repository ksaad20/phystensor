import phystensor as pt
import numpy as np

def pendulum_physics():
    print("--- Example 02: Dimensional Analysis & Derivation ---")

    # 1. Setup variables for a simple pendulum
    # Period T ≈ 2π * sqrt(L / g)
    length = pt.q(2.5, "m")
    gravity = pt.q(9.80665, "m/s^2")

    # 2. Derive the period
    # The engine calculates: sqrt([L] / [L T^-2]) -> sqrt([T^2]) -> [T]
    period = 2 * pt.utils.math_const.PI * (length / gravity)**0.5
    
    print(f"Pendulum Length: {length}")
    print(f"Local Gravity: {gravity}")
    print(f"Derived Period: {period}")
    assert period.dimensions.vector == (0, 0, 1, 0, 0, 0, 0) # Must be [Time]

    print("\n--- Fluid Dynamics: Drag Force Derivation ---")
    # Drag Equation: Fd = 1/2 * rho * v^2 * Cd * A
    # Let's solve for the Drag Coefficient (Cd), which should be dimensionless.
    
    force_measured = pt.q(150, "N")
    density_air = pt.q(1.225, "kg/m^3")
    velocity = pt.q(20, "m/s")
    area = pt.q(0.5, "m^2")

    # Cd = Fd / (0.5 * rho * v^2 * A)
    cd = force_measured / (0.5 * density_air * (velocity**2) * area)

    print(f"Measured Drag Force: {force_measured}")
    print(f"Calculated Drag Coefficient: {cd}")
    
    if cd.dimensions.is_dimensionless:
        print("Verification: Result is Dimensionless (Correct for Coefficients).")

    print("\n--- EEE: Time Constant (RC Circuit) ---")
    # Tau = R * C
    # [L^2 M T^-3 I^-2] * [L^-2 M^-1 T^4 I^2] should result in [T]
    resistor = pt.q(10, "kohm")
    capacitor = pt.q(470, "uF")
    
    tau = resistor * capacitor
    print(f"Resistance: {resistor}")
    print(f"Capacitance: {capacitor}")
    print(f"Time Constant (Tau): {tau}")
    
    # Convert to milliseconds for standard EEE reporting
    tau_ms = pt.utils.conversions.TensorConverter.scale_to(tau, "ms")
    print(f"Tau in Engineering Units: {tau_ms}")

if __name__ == "__main__":
    pendulum_physics()
