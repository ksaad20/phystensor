"""Pytest fixtures for phystensor."""

import pytest

from phystensor.io.conversion import quantity


@pytest.fixture
def force_n():
    """Return a 100 N force quantity."""
    return quantity(100, "N")


@pytest.fixture
def area_m2():
    """Return a 2 m^2 area quantity."""
    return quantity(2, "m^2")


@pytest.fixture
def resistance_ohm():
    """Return a 10 ohm resistance quantity."""
    return quantity(10, "ohm")


@pytest.fixture
def voltage_v():
    """Return a 50 V voltage quantity."""
    return quantity(50, "V")
