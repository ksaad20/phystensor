import pytest
import phystensor as pt

def test_tensor_multiplication(force_n, area_m2):
    # F * A = [M L^2 T^-2]
    work = force_n * area_m2
    assert work.dimensions.vector == (2, 1, -2, 0, 0, 0, 0)
    assert work.data == 200

def test_tensor_addition_fail(force_n, area_m2):
    # Cannot add Newtons to Square Meters
    with pytest.raises(pt.core.exceptions.DimensionalityError):
        _ = force_n + area_m2

def test_scalar_scaling(force_n):
    result = force_n * 2
    assert result.data == 200
    assert result.dimensions == force_n.dimensions

import phystensor as pt

def test_si_addition():
    # Basic validation of the 7-tuple DNA
    length1 = pt.q(10, "m")
    length2 = pt.q(5, "m")
    result = length1 + length2
    assert result.data == 15
    assert result.dimensions.vector == (1, 0, 0, 0, 0, 0, 0)

def test_maritime_units():
    # Validating the scale factor for knots
    speed = pt.q(1, "kn")
    # 1 knot is approximately 0.514444 m/s
    assert round(speed.data, 4) == 0.5144
