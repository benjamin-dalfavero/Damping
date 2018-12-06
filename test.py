import damper as dmp
from hypothesis import given
from hypothesis.strategies import floats

# tests with consideration for rounding error
smallError = lambda l, r, h: abs(l - r) <= h

# test data
ld500 = dmp.Damper(6.55, 1.0, 4.0)
sys = dmp.System(907.185, ld500)
g = 9.81 # m / s^2
a_min = 0.5 * g
a_avg = g
a_max = 1.5 * g
dt = 0.2

# test output of system against spreadsheet values
def test_min_accel():
    assert smallError(sys.accel(a_min, dt), 0.4958, 0.01)
def test_max_accel():
    assert smallError(sys.accel(a_max, dt), 10.306, 0.001)
def test_reduction_min_accel():
    assert smallError(sys.reduction(a_min, dt), 89.890, 0.00009)
def test_reduction_max_accel():
    assert smallError(sys.reduction(a_max, dt), 29.96, 0.000019)