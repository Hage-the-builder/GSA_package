import math
import sys

# Universal Database: Modulus of Elasticity (E) in Pascals (N/m^2)
WOOD_MODULUS = {
    "pine": 11.0e9,       # Southern Yellow Pine
    "oak": 12.4e9,        # Red Oak
    "fir": 13.0e9         # Douglas Fir
}

# Crushing strength limit parallel to the wood grain (Pascals)
WOOD_CRUSH_LIMIT = {
    "pine": 36.2e6,
    "oak": 49.6e6,
    "fir": 42.8e6
}

def main():
    print("=== Universal Frame Cell Structural Analyzer ===")
    print("Open-source tool to calculate buckling and crushing limits.")

    # 1. Gather Athlete Metrics
    try:
        wood = input("Wood type (pine/oak/fir) [default: pine]: ").strip().lower() or "pine"
        if wood not in WOOD_MODULUS:
            sys.exit("Error: Material type not registered in global database.")

        weight_input = input("Athlete weight in lbs [default: 250]: ").strip()
        weight_lbs = float(weight_input) if weight_input else 250.0
        mass_kg = weight_lbs * 0.453592

        vel_input = input("Landing impact velocity in m/s [default: 2.0]: ").strip()
        velocity = float(vel_input) if vel_input else 2.0

        posts_input = input("Number of active posts holding the bar (2 or 4) [default: 2]: ").strip()
        active_posts = int(posts_input) if posts_input else 2
        if active_posts not in (2, 4):
            sys.exit("Error: Active posts must be either 2 or 4.")


        # 2. Gather Geometric Layout Specs
        height_in = input("Post height in feet [default: 8.0]: ").strip()
        height_ft = float(height_in) if height_in else 8.0
        post_height = height_ft * 0.3048  # Convert feet to meters

        thick_in = input("Square timber width/thickness in inches [default: 3.5]: ").strip()
        thick_val = float(thick_in) if thick_in else 3.5
        post_thickness = thick_val * 0.0254  # Convert inches to meters

        bar_in = input("Outside diameter of the bar pipe in inches [default: 1.315]: ").strip()
        bar_val = float(bar_in) if bar_in else 1.315
        bar_diameter = bar_val * 0.0254  # Convert inches to meters

    except ValueError:
        sys.exit("Error: Numerical data processing failed. Please check your inputs.")

    # 3. run universal math modules
    try:
        single_post_limit = calculate_column_buckling(post_thickness, post_height, wood)
        total_impact_force = simulate_dynamic_impact(mass_kg, velocity)

        total_gym_capacity = single_post_limit * active_posts
        force_per_block = total_impact_force / 2.0

        # Clamping block width matches the structural timber post width flush
        actual_bearing_stress = calculate_bearing_stress(force_per_block, bar_diameter, post_thickness)
    except ValueError as e:
        sys.exit(f"Engineering Boundary Failure: {e}")

    # 4. Process final safety factor margins
    allowed_crush = WOOD_CRUSH_LIMIT[wood]
    buckling_safety_factor = total_gym_capacity / total_impact_force
    bearing_safety_factor = allowed_crush / actual_bearing_stress

    # 5. Display performance ledger
    print("\n=== SYSTEM SAFETY REPORT ===")
    print(f"Single Column Buckling Limit : {single_post_limit:.1f} Newtons")
    print(f"Total Framework Capacity     : {total_gym_capacity:.1f} Newtons")
    print(f"Peak Dynamic Landing Force   : {total_impact_force:.1f} Newtons")
    print(f"Interface Crushing Stress    : {(actual_bearing_stress / 1e6):.2f} MPa")
    print(f"Buckling Safety Factor       : {buckling_safety_factor:.2f} SF")
    print(f"Bearing Safety Factor        : {bearing_safety_factor:.2f} SF")

    if buckling_safety_factor < 1.0 or bearing_safety_factor < 1.0:
        print("\n❌ CRITICAL: Structural bounds breached! Design will collapse under load.")
    else:
        print("\n✅ VERIFIED: Framework configurations pass all safety margins.")


def calculate_column_buckling(thickness, height, wood_type):
    """Computes Euler's critical column buckling load for an individual timber member."""
    if thickness <= 0 or height <= 0:
        raise ValueError("Physical dimensions must be absolute positive metrics.")

    wood = wood_type.lower().strip()
    if wood not in WOOD_MODULUS:
        raise ValueError("Requested material species not found in regional registries.")

    e_value = WOOD_MODULUS[wood]
    # Area Moment of Inertia for a universal square shape: I = a^4 / 12
    inertia_i = (thickness ** 4) / 12.0
    # Standard Euler Buckling Equation
    return (math.pi ** 2 * e_value * inertia_i) / (height ** 2)


def simulate_dynamic_impact(mass, velocity, stopping_dist=0.02):
    """Calculates peak dynamic kinetic impact load using the Work-Energy Principle."""
    if mass <= 0 or velocity < 0 or stopping_dist <= 0:
        raise ValueError("Mass, velocity, and deceleration parameters must be valid numbers.")

    # Convert kinetic energy change into structural node forces
    kinetic_energy = 0.5 * mass * (velocity ** 2)
    impact_force = kinetic_energy / stopping_dist
    static_gravity_force = mass * 9.81
    return impact_force + static_gravity_force


def calculate_bearing_stress(force, bar_dia, block_w):
    """Calculates internal crushing bearing stress localized at the bar-to-block surface interface."""
    if force <= 0 or bar_dia <= 0 or block_w <= 0:
        raise ValueError("Force vectors and geometric interface contact areas must be positive numbers.")

    # Direct rectangular bearing footprint area = pipe outer diameter * block width
    bearing_area = bar_dia * block_w
    return force / bearing_area


if __name__ == "__main__":
    main()
