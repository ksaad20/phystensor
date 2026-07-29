"""Maritime vessel performance analysis example."""

import phystensor as pt
from phystensor.units.constants import g_n


def vessel_performance_analysis():
    """Run hull, power, and compliance calculations for a vessel."""
    print("--- Example 03: Maritime Hull & Power Physics ---")

    # 1. Displacement & Buoyancy
    water_density = pt.q(1025, "kg/m^3")  # Average Seawater
    displaced_volume = pt.q(45000, "m^3")

    buoyant_force = water_density * g_n * displaced_volume
    print("Total Displacement (Volume): " + str(displaced_volume))
    print("Buoyant Force: " + str(buoyant_force))

    displacement_ton = pt.utils.conversions.TensorConverter.scale_to(
        buoyant_force / g_n, "ton"
    )
    print("Vessel Deadweight (DWT equivalent): " + str(displacement_ton))

    # 2. Hull Resistance (Simplified Admiralty Coefficient Method)
    speed = pt.q(14, "kn")
    admiralty_coefficient = pt.q(450, "")  # Dimensionless efficiency factor

    power_required = (
        (displacement_ton.data ** (2 / 3)) * (speed**3)
    ) / admiralty_coefficient

    p_kw = pt.q(power_required.data, "kW")
    print("\nTarget Speed: " + str(speed))
    print("Estimated Propulsion Power: " + str(p_kw))

    # 3. Fuel Consumption & Operational Cost
    sfoc = pt.q(185, "g/kWh")

    fuel_rate = p_kw * sfoc
    fuel_rate_ton_day = pt.utils.conversions.TensorConverter.scale_to(
        fuel_rate, "ton/day"
    )
    print("Fuel Consumption Rate: " + str(fuel_rate_ton_day))

    # 4. Maritime Compliance: Carbon Intensity Indicator (CII)
    voyage_distance = pt.q(500, "nmi")
    hfo_carbon_factor = pt.q(3.114, "")  # tCO2 / tFuel

    total_fuel_ton = fuel_rate * (voyage_distance / speed)
    total_co2 = total_fuel_ton * hfo_carbon_factor

    cii_metric = total_co2 / (displacement_ton * voyage_distance)
    cii_scaled = pt.utils.conversions.TensorConverter.scale_to(
        cii_metric, "g/(ton*nmi)"
    )

    print("\n--- Voyage Compliance ---")
    print("Total CO2 Emissions: " + str(total_co2))
    print("CII Result: " + str(cii_scaled))


if __name__ == "__main__":
    vessel_performance_analysis()
