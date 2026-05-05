import phystensor as pt

def test_quantity_parsing():
    q = pt.q(10, "kN")
    assert q.data == 10000
    assert q.dimensions.vector == (1, 1, -2, 0, 0, 0, 0)

def test_complex_string_parsing():
    q = pt.q(1, "kg*m/s^2")
    assert q.dimensions.vector == (1, 1, -2, 0, 0, 0, 0)
