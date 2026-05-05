import phystensor as pt
import json
from phystensor.core.exceptions import PhystensorError

def simulate_api_request(payload_json: str):
    """
    Simulates a Xylema API endpoint receiving a POST request.
    The goal is to sterilize incoming data into the phystensor ecosystem.
    """
    print("--- Xylema API: Inbound Sterilization Layer ---")
    
    try:
        data = json.loads(payload_json)
        
        # 1. THE STERILIZATION PROCESS
        # We transform raw JSON floats/lists into validated PhysicalTensors.
        # This acts as a 'physical schema' validation.
        
        vessel_speed = pt.q(data.get("speed"), data.get("speed_unit", "kn"))
        fuel_mass = pt.q(data.get("fuel"), data.get("fuel_unit", "ton"))
        voyage_dist = pt.q(data.get("distance"), data.get("dist_unit", "nmi"))
        
        print(f"Validated Input: Speed={vessel_speed}, Fuel={fuel_mass}")

        # 2. THE LOGIC LAYER (Century-Proof)
        # Once sterilized, we can perform math with zero fear of unit mismatch.
        time_elapsed = voyage_dist / vessel_speed
        consumption_rate = fuel_mass / time_elapsed
        
        # 3. THE OUTBOUND SERIALIZATION
        # Convert results back to standard SI or specified units for the API response.
        response = {
            "status": "success",
            "results": {
                "hourly_rate_kg_h": pt.utils.conversions.TensorConverter.scale_to(consumption_rate, "kg/h").data.tolist(),
                "voyage_duration_hours": pt.utils.conversions.TensorConverter.scale_to(time_elapsed, "h").data.tolist(),
                "si_dimensions": str(consumption_rate.dimensions)
            }
        }
        return json.dumps(response, indent=2)

    except (PhystensorError, ValueError) as e:
        # Catching physical law violations (e.g., trying to add Speed to Distance)
        # or unit lookup failures (e.g., 'kilogams' typo).
        return json.dumps({
            "status": "error",
            "error_type": "PhysicalSterilizationFailure",
            "message": str(e)
        }, indent=2)

# --- SCENARIO A: VALID DATA ---
valid_payload = json.dumps({
    "speed": 12.5, "speed_unit": "kn",
    "fuel": 45.0, "fuel_unit": "ton",
    "distance": 500, "dist_unit": "nmi"
})

# --- SCENARIO B: MALFORMED PHYSICS (Unit Typo) ---
invalid_payload = json.dumps({
    "speed": 12.5, "speed_unit": "knots_typo", # Will trigger UnitNotFoundError
    "fuel": 45.0, "fuel_unit": "ton",
    "distance": 500, "dist_unit": "nmi"
})

if __name__ == "__main__":
    print("\n[Processing Valid Payload]")
    print(simulate_api_request(valid_payload))
    
    print("\n[Processing Invalid Payload]")
    print(simulate_api_request(invalid_payload))
