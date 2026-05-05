import phystensor as pt

def vessel_performance_analysis():
    print("--- Example 03: Maritime Hull & Power Physics ---")

    # 1. Displacement & Buoyancy
    # Archimedes Principle: Buoyant Force = density * gravity * displaced_volume
    water_density = pt.q(1025, "kg/m^3")  # Average Seawater
    displaced_volume = pt.q(45000, "m^3")
    from phystensor.units.constants import g_n

    buoyant_force = water_density * g_n * displaced_volume
    print(f"Total Displacement (Volume): {displaced_volume}")
    print(f"Buoyant Force: {buoyant_force}")
    
    # Convert force to 'ton' (Metric Ton-force) for standard shipping terminology
    displacement_ton = pt.utils.conversions.TensorConverter.scale_to(buoyant_force / g_n, "ton")
    print(f"Vessel Deadweight (DWT equivalent): {displacement_ton}")

    # 2. Hull Resistance (Simplified Admiralty Coefficient Method)
    # P = (D^(2/3) * v^3) / C
    # Where P is Power, D is displacement, v is speed, and C is the coefficient.
    
    speed = pt.q(14, "kn")
    admiralty_coefficient = pt.q(450, "") # Dimensionless efficiency factor
    
    # Power required proportional to V^3
    # Note: pt.q handles the DWT unit conversion internally
    power_required = ((displacement_ton.data**(2/3)) * (speed**3)) / admiralty_coefficient
    
    # Currently, 'power_required' is a float because of the empirical coefficient logic.
    # Let's wrap it back into a PhysicalTensor in kilowatts.
    p_kw = pt.q(power_required.data, "kW")
    print(f"\nTarget Speed: {speed}")
    print(f"Estimated Propulsion Power: {p_kw}")

    # 3. Fuel Consumption & Operational Cost
    # Specific Fuel Oil Consumption (SFOC)
    sfoc = pt.q(185, "g/kWh")
    
    # Fuel Flow Rate = Power * SFOC
    fuel_rate = p_kw * sfoc
    print(f"Fuel Consumption Rate: {pt.utils.conversions.TensorConverter.scale_to(fuel_rate, 'ton/day')}")

    # 4. Maritime Compliance: Carbon Intensity Indicator (CII)
    # CII = (Fuel_Mass * Carbon_Factor) / (Capacity * Distance)
    voyage_distance = pt.q(500, "nmi")
    hfo_carbon_factor = pt.q(3.114, "") # tCO2 / tFuel
    
    total_fuel_ton = (fuel_rate * (voyage_distance / speed))
    total_co2 = total_fuel_ton * hfo_carbon_factor
    
    cii_metric = total_co2 / (displacement_ton * voyage_distance)
    
    print(f"\n--- Voyage Compliance ---")
    print(f"Total CO2 Emissions: {total_co2}")
    print(f"CII Result: {pt.utils.conversions.TensorConverter.scale_to(cii_metric, 'g/(ton*nmi)')}")

if __name__ == "__main__":
    vessel_performance_analysis()
