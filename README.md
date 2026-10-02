# Gym Structural Analyzer

[![PyPI version](https://img.shields.io/pypi/v/gym-structural-analyzer.svg)](https://pypi.org/project/gym-structural-analyzer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)


**Gym Structural Analyzer** is an open-source Python package I built to help check the structural strength of wooden frames before building them.

The project started from a simple question: **How much force can a wooden calisthenics structure actually handle?**

Instead of relying only on the weight of the person using it, the program looks at things like **buckling, material properties, impact forces, and bearing stress** to give a better idea of how a design will behave under load.

## Installation

The package is available on PyPI:

```bash
pip install gym-structural-analyzer
```

## What It Can Do

* **Column Buckling** : Calculates the critical load at which a wooden post could buckle.
* **Dynamic Impact** : Estimates peak forces caused by movement and sudden deceleration rather than only using static body weight.
* **Multiple Wood Types** : Includes material data for woods such as Southern Yellow Pine, Red Oak, and Douglas Fir.
* **Custom Dimensions** : Test different post sizes, heights, and material choices.
* **Input Validation** : Checks inputs and catches invalid dimensions or material selections.

## Usage

You can run the program from the terminal:

```bash
python gym-structural-analyzer.py
```

You can also use the calculation functions directly in another Python program:

```python
from project import calculate_column_buckling, simulate_dynamic_impact

# 4x4 wooden post
# Actual dimensions: 3.5" × 3.5"
# Height: 8 ft
wood_type = "pine"
post_thickness = 0.0889
post_height = 2.4384

p_critical = calculate_column_buckling(
    post_thickness,
    post_height,
    wood_type
)

print(f"Critical Buckling Load: {p_critical:.1f} N")
```

## How the Math Works

The program currently focuses on two important structural failure modes.

### 1. Column Buckling

A tall, slender wooden post can fail by buckling rather than simply being crushed. The program uses the Euler buckling equation:

$$
P_{cr} = \frac{\pi^2EI}{L^2}
$$

where:

* **E** = Modulus of Elasticity of the wood
* **I** = Area Moment of Inertia
* **L** = Length of the post

For a square cross-section:

$$
I = \frac{a^4}{12}
$$

This lets the program compare different post sizes and heights and see how they affect the critical buckling load.

### 2. Bearing Stress

The program also checks localized forces where components connect to the wooden frame.

For example, when a pull-up bar transfers force into a wooden support, the force is concentrated over a relatively small area. The bearing calculation checks whether that local stress could exceed the material's allowable strength.

## Testing

The project includes automated tests using `pytest`.

Run the tests with:

```bash
pytest test_gym_structural_analyzer.py
```

## Why I Built It

I originally started working on this because I wanted to build a **wooden calisthenics gym in my own backyard**.

I didn't want to just guess whether the posts and bars would be strong enough. I wanted to understand the engineering behind the design and build something that I could test mathematically before cutting and assembling the wood.

That turned into this Python project.

What started as calculations for one structure became a small engineering tool that can be used to experiment with different materials, dimensions, and loading conditions.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

