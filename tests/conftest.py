import pytest
import phystensor as pt

@pytest.fixture
def force_n():
    return pt.q(100, "N")

@pytest.fixture
def area_m2():
    return pt.q(2, "m^2")

@pytest.fixture
def resistance_ohm():
    return pt.q(10, "ohm")

@pytest.fixture
def voltage_v():
    return pt.q(50, "V")
