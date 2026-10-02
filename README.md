# Gym Structural Analyzer 


A universal, open-source Python package designed to stress-test and structurally verify backyard calisthenics gyms or timber frames prior to physical carpentry construction. 

This engine uses discrete engineering mechanics (Euler's Column Buckling Theorem and the Work-Energy Principle) to calculate if vertical wood supports will buckle or crush under dynamic athletic loads.

## Installation

The package is officially published to the global Python Package Index (PyPI). You can install it directly onto any machine terminal globally by running:

```bash
pip install gym-structural-analyzer
```

## Features

* **Universal Math Modules:** Standalone calculation modules that accept any custom timber dimensions, lumber species, or player weights.
* **Dynamic Impact Simulation:** Maps deceleration bounds to calculate instantaneous peak impact force spikes from moving kinetic energy, bypassing simple static weight estimations.
* **Material Integrity Registries:** Cross-references calculations against built-in industrial engineering datasets for Southern Yellow Pine, Red Oak, and Douglas Fir.
* **Input Protection Gates:** Bulletproof error handling that catches illegal structural geometry or material choices safely.

## Usage

To run the interactive terminal interface locally:
```bash
python gym-structural-analyzer.py
```

### Example Code Integration
If you are building your own engineering pipeline, you can import and call the underlying physics calculators directly inside your code scripts:

```python
from project import calculate_column_buckling, simulate_dynamic_impact

# Test a standard 4x4 pine column (3.5" thickness = 0.0889m) at an 8ft height (2.4384m)
wood_type = "pine"
post_thickness = 0.0889 
post_height = 2.4384

p_critical = calculate_column_buckling(post_thickness, post_height, wood_type)
print(f"Critical Buckling Point: {p_critical:.1f} Newtons")
```

## Underlying Engineering Physics

The codebase operates across two primary mechanical failure modes:

### 1. Column Buckling (Euler's Theorem)
When an athlete executes explosive movements, vertical pillars experience severe axial compression load. If a pillar is too tall or too thin, it will bow and violently snap outward. The program tracks this boundary using:
\[P_{cr} = \frac{\pi^2 E I}{L^2}\]
Where E represents the wood material stiffness (Modulus of Elasticity), I is the cross-sectional shape's Area Moment of Inertia (\(I = \frac{a^4}{12}\) for square profiles), and L is the vertical height of the post.

### 2. Local Bearing Crushing Stress
Where the metal pull-up bar passes through the wooden split capping block mechanism, the downward force vector behaves like a miniature crushing cylinder. The software checks this localized bearing footprint to ensure internal stresses stay safely below material fiber boundaries:
\[\text{Stress} = \frac{\text{Force}}{\text{Area}}\]
Where Area is calculated dynamically using the pipe outside diameter multiplied by the exact contact block surface width.

## Automated Testing

This package uses a comprehensive Test-Driven Development (TDD) layout. To run the automated unit testing validation loops and ensure the math calculations pass cleanly:

```bash
pytest test_gym_structural_analyzer.py
```

## License

Distributed under the **MIT License**. See `LICENSE` for more details.

