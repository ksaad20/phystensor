import phystensor as pt

def test_knot_to_ms():
    speed_kn = pt.q(1, "kn")
    # 1 knot = 0.514444 m/s
    assert abs(speed_kn.data - 0.514444) < 1e-5

def test_unit_rescaling():
    # Test internal conversion utility
    dist = pt.q(1, "km")
    scaled = pt.utils.conversions.TensorConverter.scale_to(dist, "m")
    assert scaled.data == 1000
