"""Example 02: Dimensional analysis and derived physical quantities."""

import phystensor as pt


def pendulum_physics() -> None:
    """Demonstrate dimensional analysis using several physics examples."""
    print("--- Example 02: Dimensional Analysis & Derivation ---")

    # ------------------------------------------------------------------
    # Simple Pendulum
    # Period: T = 2π * sqrt(L / g)
    # ------------------------------------------------------------------
    length = pt.q(2.5, "m")
    gravity = pt.q(9.80665, "m/s^2")

    period = 2 * pt.utils.math_const.PI * (length / gravity) ** 0.5

    print(f"Pendulum Length: {length}")
    print(f"Local Gravity: {gravity}")
    print(f"Derived Period: {period}")

    assert period.dimensions.vector == (
        0,
        0,
        1,
        0,
        0,
        0,
        0,
    )

    # ------------------------------------------------------------------
    # Fluid Dynamics
    # Drag equation:
    # Fd = 1/2 * ρ * v² * Cd * A
    # Solve for Cd.
    # ------------------------------------------------------------------
    print("\n--- Fluid Dynamics: Drag Force Derivation ---")

    force_measured = pt.q(150, "N")
    density_air = pt.q(1.225, "kg/m^3")
    velocity = pt.q(20, "m/s")
    area = pt.q(0.5, "m^2")

    cd = force_measured / (
        0.5 * density_air * (velocity**2) * area
    )

    print(f"Measured Drag Force: {force_measured}")
    print(f"Calculated Drag Coefficient: {cd}")

    if cd.dimensions.is_dimensionless:
        print(
            "Verification: Result is dimensionless "
            "(correct for coefficients)."
        )

    # ------------------------------------------------------------------
    # RC Circuit
    # τ = R × C
    # ------------------------------------------------------------------
    print("\n--- EEE: Time Constant (RC Circuit) ---")

    resistor = pt.q(10, "kohm")
    capacitor = pt.q(470, "uF")

    tau = resistor * capacitor

    print(f"Resistance: {resistor}")
    print(f"Capacitance: {capacitor}")
    print(f"Time Constant (Tau): {tau}")

    tau_ms = pt.utils.conversions.TensorConverter.scale_to(
        tau,
        "ms",
    )

    print(f"Tau in Engineering Units: {tau_ms}")


if __name__ == "__main__":
    pendulum_physics()
