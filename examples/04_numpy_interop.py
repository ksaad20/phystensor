"""NumPy vectorization and interoperability example."""

import numpy as np

import phystensor as pt


def sensor_array_processing():
    """Demonstrate NumPy array integration with PhysicalTensors."""
    print("--- Example 04: NumPy Vectorization & Interoperability ---")

    # 1. Creating Tensors from NumPy Arrays
    # Imagine these are readings from a 5-storey mushroom facility's thermal sensors
    raw_data = np.array([22.5, 23.1, 22.8, 24.0, 23.5])
    temperatures = pt.q(raw_data, "degC")

    print("Sensor Grid Temps: " + str(temperatures))
    print("Data Shape: " + str(temperatures.data.shape))

    # 2. Vectorized Arithmetic
    # Apply a calibration offset to the entire array at once
    offset = pt.q(0.5, "K")
    calibrated_temps = temperatures + offset
    print("Calibrated Grid: " + str(calibrated_temps))

    # 3. Broadcasting Logic
    # Multiplying a vector by a scalar tensor
    # Calculate thermal energy (Q = m * c * delta_T) for a grid of soil samples
    mass_per_sample = pt.q(2.0, "kg")
    specific_heat_capacity = pt.q(4184, "J/(kg*K)")  # Water-heavy substrate
    delta_t = pt.q([2, 5, 1, 3, 4], "K")

    energy_grid = mass_per_sample * specific_heat_capacity * delta_t
    print("\nEnergy Absorption Grid: " + str(energy_grid))

    # 4. NumPy Method Delegation
    # phystensor wraps common NumPy reduction operations while preserving units
    max_energy = pt.q(np.max(energy_grid.data), energy_grid.dimensions)
    mean_energy = pt.q(np.mean(energy_grid.data), energy_grid.dimensions)

    print("Peak Energy: " + str(max_energy))
    print("Average Energy: " + str(mean_energy))

    # 5. Slicing and Manipulation
    # Accessing specific sensors (e.g., the top floor of the facility)
    top_floor_energy = energy_grid[0:2]
    print("Top Floor Readings: " + str(top_floor_energy))

    # 6. Safety Check: Incompatible Array Operations
    try:
        # Attempting to add a dimensionless NumPy array to a PhysicalTensor
        energy_grid + np.array([1, 2, 3, 4, 5])
    except pt.core.exceptions.DimensionalityError as e:
        print("\nValidation Success: Prevented adding naked numbers to energy grid.")
        print("Error: " + str(e))


if __name__ == "__main__":
    sensor_array_processing()
