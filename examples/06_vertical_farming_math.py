import phystensor as pt

def mushroom_facility_analysis():
    print("--- Xylema Agri-Tech: Vertical Farming Thermodynamics ---")

    # 1. FACILITY DIMENSIONS (5-Storey Vertical Leverage)
    floor_area = pt.q(200, "m^2")
    height_per_floor = pt.q(3.5, "m")
    num_floors = 5
    total_volume = floor_area * height_per_floor * num_floors
    
    print(f"Total Facility Volume: {total_volume}")

    # 2. EVAPORATIVE COOLING LOAD
    # To maintain 90% humidity for mushroom pinning, we need precise water injection.
    # We calculate the cooling power extracted from the room via Latent Heat.
    water_evap_rate = pt.q(12.5, "kg/h")
    latent_heat_water = pt.q(2260, "kJ/kg") # L_v at standard growth temp
    
    # Q_dot = m_dot * L
    cooling_load = water_evap_rate * latent_heat_water
    print(f"Evaporative Cooling Rate: {cooling_load}")
    
    # Convert to BTU/h for HVAC equipment procurement (Common in Bangladesh/India)
    hvac_requirement = pt.utils.conversions.TensorConverter.scale_to(cooling_load, "BTU/h")
    print(f"HVAC Requirement: {hvac_requirement}")

    # 3. CO2 CONCENTRATION MANAGEMENT
    # Mushrooms produce CO2; we must calculate the air exchange rate.
    # Production rate: 0.5 grams per hour per kg of substrate
    total_substrate = pt.q(5000, "kg")
    co2_production_rate = pt.q(0.5, "g/(kg*h)") * total_substrate
    
    print(f"Total CO2 Production: {co2_production_rate}")

    # 4. SUBSTRATE THERMAL MASS (The "Ampere©" Manufacturing crossover)
    # Calculating the energy required to pasteurize the substrate (60°C to 100°C)
    t_initial = pt.q(25, "degC")
    t_pasteurize = pt.q(100, "degC")
    delta_t = t_pasteurize - t_initial
    
    # Specific heat of substrate (assumed near water)
    cp_substrate = pt.q(3.8, "kJ/(kg*K)")
    
    total_energy_required = total_substrate * cp_substrate * delta_t
    print(f"Pasteurization Energy Needed: {total_energy_required}")
    
    # Power required to do this in 2 hours
    time_window = pt.q(2, "h")
    boiler_power = total_energy_required / time_window
    print(f"Required Boiler Rating: {pt.utils.conversions.TensorConverter.scale_to(boiler_power, 'kW')}")

if __name__ == "__main__":
    mushroom_facility_analysis()
