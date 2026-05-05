import pytest
# Use direct imports to bypass the __init__.py circular loop
from phystensor.io.conversion import quantity

@pytest.fixture
def force_n():
    return quantity(100, "N")

@pytest.fixture
def area_m2():
    return quantity(2, "m^2")

@pytest.fixture
def resistance_ohm():
    return quantity(10, "ohm")

@pytest.fixture
def voltage_v():
    return quantity(50, "V")
