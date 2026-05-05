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
