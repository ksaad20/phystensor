import pytest
from phystensor.units.dimensions import Dimensions

def test_dimension_addition():
    # L + L = L (Vector stays same)
    d1 = Dimensions((1, 0, 0, 0, 0, 0, 0))
    assert d1 + d1 == d1

def test_dimension_multiplication():
    # L * M = LM
    length = Dimensions((1, 0, 0, 0, 0, 0, 0))
    m = Dimensions((0, 1, 0, 0, 0, 0, 0))
    result = length * m
    assert result.vector == (1, 1, 0, 0, 0, 0, 0)

def test_dimension_inversion():
    # T -> T^-1
    t = Dimensions((0, 0, 1, 0, 0, 0, 0))
    assert (-t).vector == (0, 0, -1, 0, 0, 0, 0)
