import pytest
import math
import importlib


analyzer = importlib.import_module("gym-structural-analyzer")

def test_calculate_column_buckling():

    p_critical = analyzer.calculate_column_buckling(0.0889, 2.4384, "pine")
    assert abs(p_critical - 95040.4) < 5.0

    p_oak = analyzer.calculate_column_buckling(0.0889, 2.4384, "oak")
    assert p_oak > p_critical

    with pytest.raises(ValueError):
        analyzer.calculate_column_buckling(-0.0889, 2.4384, "pine")
    with pytest.raises(ValueError):
        analyzer.calculate_column_buckling(0.0889, 2.4384, "fake_wood")


def test_simulate_dynamic_impact():

    total_force = analyzer.simulate_dynamic_impact(113.398, 2.0, 0.02)
    assert abs(total_force - 12452.2) < 5.0

    with pytest.raises(ValueError):
        analyzer.simulate_dynamic_impact(-10, 2.0)


def test_calculate_bearing_stress():

    stress = analyzer.calculate_bearing_stress(6226.1, 0.0334, 0.0889)
    assert abs(stress - 2096813.1) < 5.0

    with pytest.raises(ValueError):
        analyzer.calculate_bearing_stress(6226.1, -0.0334, 0.0889)
