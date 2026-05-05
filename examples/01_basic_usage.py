import phystensor as pt

def main():
    print("--- Phystensor Example 01: Basic Usage ---")

    # 1. Instantiation via the 'q' (quantity) alias
    # This is the "Low Labor" way to create unit-aware tensors.
    distance = pt.q(100, "m")
    time = pt.q(9.58, "s")  # Usain Bolt's world record pace

    print(f"Distance: {distance}")
    print(f"Time: {time}")

    # 2. Automatic Dimensional Inference
    # Multiplying or dividing automatically derives the correct SI-vector.
    velocity = distance / time
    print(f"Calculated Velocity: {velocity}") 

    # 3. Unit Safety (The "Century-Proof" Guardrail)
    # Attempting to add mismatched units raises a DimensionalityError.
    try:
        invalid_op = distance + time
    except pt.core.exceptions.DimensionalityError as e:
        print(f"\nCaught Expected Error: {e}")

    # 4. Working with Arrays (NumPy Integration)
    # Phystensor handles multi-dimensional arrays just as easily as scalars.
    forces = pt.q([10.0, 20.0, 30.0], "N")
    mass = pt.q(5.0, "kg")
    
    acceleration = forces / mass
    print(f"\nAcceleration Array: {acceleration}")

    # 5. On-the-fly Conversion
    # Use the 'scale_to' utility for industrial reporting.
    speed_kmh = pt.utils.conversions.TensorConverter.scale_to(velocity, "km/h")
    print(f"Velocity in km/h: {speed_kmh}")

    # 6. Using Fundamental Constants
    # Constants are pre-clothed in their SI-dimensions.
    from phystensor.units.constants import c
    energy = mass * (c**2)
    print(f"\nRest Energy (E=mc^2): {energy}")

if __name__ == "__main__":
    main()
