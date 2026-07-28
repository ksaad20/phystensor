"""Example 01: Basic usage of Phystensor."""

import phystensor as pt


def main() -> None:
    """Run the basic Phystensor demonstration."""
    print("--- Phystensor Example 01: Basic Usage ---")

    # ------------------------------------------------------------------
    # 1. Create unit-aware quantities.
    # ------------------------------------------------------------------
    distance = pt.q(100, "m")
    time = pt.q(9.58, "s")

    print(f"Distance: {distance}")
    print(f"Time: {time}")

    # ------------------------------------------------------------------
    # 2. Automatic dimensional derivation.
    # Velocity = distance / time
    # ------------------------------------------------------------------
    velocity = distance / time

    print(f"Calculated Velocity: {velocity}")

    # ------------------------------------------------------------------
    # 3. Dimensional safety.
    # Adding incompatible physical quantities should fail.
    # ------------------------------------------------------------------
    try:
        _ = distance + time
    except pt.core.exceptions.DimensionalityError as error:
        print(f"\nCaught Expected Error: {error}")

    # ------------------------------------------------------------------
    # 4. NumPy-compatible tensor operations.
    # ------------------------------------------------------------------
    forces = pt.q(
        [10.0, 20.0, 30.0],
        "N",
    )

    mass = pt.q(5.0, "kg")

    acceleration = forces / mass

    print(f"\nAcceleration Array: {acceleration}")

    # ------------------------------------------------------------------
    # 5. Convert derived quantities.
    # ------------------------------------------------------------------
    speed_kmh = pt.convert(
        velocity,
        "km/h",
    )

    print(f"Velocity in km/h: {speed_kmh}")

    # ------------------------------------------------------------------
    # 6. Use physical constants.
    # E = mc²
    # ------------------------------------------------------------------
    c = pt.q(299792458, "m/s")

    energy = mass * (c**2)

    print(f"\nRest Energy (E = mc²): {energy}")


if __name__ == "__main__":
    main()
