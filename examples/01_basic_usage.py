"""Example 01: Basic usage of Phystensor."""

import phystensor as pt
from phystensor.units.constants import c


def main() -> None:
    """Run the basic Phystensor demonstration."""
    print("--- Phystensor Example 01: Basic Usage ---")

    # 1. Instantiation via the 'q' (quantity) alias.
    distance = pt.q(100, "m")
    time = pt.q(9.58, "s")  # Usain Bolt's world-record pace

    print(f"Distance: {distance}")
    print(f"Time: {time}")

    # 2. Automatic dimensional inference.
    velocity = distance / time
    print(f"Calculated Velocity: {velocity}")

    # 3. Unit safety.
    try:
        distance + time
    except pt.core.exceptions.DimensionalityError as error:
        print(f"\nCaught Expected Error: {error}")

    # 4. NumPy-compatible arrays.
    forces = pt.q([10.0, 20.0, 30.0], "N")
    mass = pt.q(5.0, "kg")

    acceleration = forces / mass
    print(f"\nAcceleration Array: {acceleration}")

    # 5. Unit conversion.
    speed_kmh = pt.utils.conversions.TensorConverter.scale_to(
        velocity,
        "km/h",
    )
    print(f"Velocity in km/h: {speed_kmh}")

    # 6. Using physical constants.
    energy = mass * (c**2)
    print(f"\nRest Energy (E = mc²): {energy}")


if __name__ == "__main__":
    main()
