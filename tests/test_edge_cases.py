import pytest
import phystensor as pt
import numpy as np

def test_dimensionless_ops():
    # Adding two dimensionless quantities should work
    a = pt.q(1, "")
    b = pt.q(2, "")
    assert (a + b).data == 3

def test_zero_tensor():
    # Operations with zero should preserve dimensions
    z = pt.q(0, "N")
    f = pt.q(10, "N")
    assert (z + f).dimensions == f.dimensions

def test_extreme_precision():
    # Astrophysics scale
    light_year = pt.q(1, "ly")
    fermi = pt.q(1, "femtometer")
    ratio = light_year / fermi
    assert ratio.data > 1e30
