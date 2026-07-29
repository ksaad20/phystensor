import phystensor as pt


def mushroom_facility_analysis():
    """Run thermodynamic calculations for a mushroom cultivation facility."""
    print("--- Vertical Farming Thermodynamics ---")

    # 1. FACILITY DIMENSIONS (5-Storey Vertical Leverage)
    floor_area = pt.q(200, "m^2")
    height_per_floor = pt.q(3.5, "m")
    num_floors = 5
    total_volume = floor_area * height_per_floor * num_floors

    print("Total Facility Volume: " + str(total_volume))

    # 2. EVAPORATIVE COOLING LOAD
    water_evap_rate = pt.q(12.5, "kg/h")
    latent_heat_water = pt.q(2260, "kJ/kg")  # L_v at standard growth temp

    cooling_load = water_evap_rate * latent_heat_water
    print("Evaporative Cooling Rate: " + str(cooling_load))

    # Convert to BTU/h for HVAC equipment procurement
    hvac_requirement = pt.utils.conversions.TensorConverter.scale_to(
        cooling_load, "BTU/h"
    )
    print("HVAC Requirement: " + str(hvac_requirement))

    # 3. CO2 CONCENTRATION MANAGEMENT
    total_substrate = pt.q(5000, "kg")
    co2_production_rate = pt.q(0.5, "g/(kg*h)") * total_substrate

    print("Total CO2 Production: " + str(co2_production_rate))

    # 4. SUBSTRATE THERMAL MASS
    t_initial = pt.q(25, "degC")
    t_pasteurize = pt.q(100, "degC")
    delta_t = t_pasteurize - t_initial

    cp_substrate = pt.q(3.8, "kJ/(kg*K)")

    total_energy_required = total_substrate * cp_substrate * delta_t
    print("Pasteurization Energy Needed: " + str(total_energy_required))

    # Power required to do this in 2 hours
    time_window = pt.q(2, "h")
    boiler_power = total_energy_required / time_window
    boiler_kw = pt.utils.conversions.TensorConverter.scale_to(
        boiler_power, "kW"
    )
    print("Required Boiler Rating: " + str(boiler_kw))


if __name__ == "__main__":
    mushroom_facility_analysis()
