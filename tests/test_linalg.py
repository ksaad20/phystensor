import pytest
import phystensor as pt
import numpy as np

def test_ohm_law_solver(resistance_ohm, voltage_v):
    # V = I * R -> I = V / R
    current = pt.linalg.solve(resistance_ohm, voltage_v)
    assert current.data == 5.0
    assert current.dimensions.vector == (0, 0, 0, 1, 0, 0, 0) # Amperes

def test_matrix_inversion():
    # Inverse of Ohm is Siemens
    a = pt.q([[2, 0], [0, 2]], "ohm")
    a_inv = pt.linalg.inv(a)
    assert a_inv.dimensions.vector == (-2, -1, 3, 2, 0, 0, 0) # S
    assert np.allclose(a_inv.data, [[0.5, 0], [0, 0.5]])
