'''
plot reduction of acceleration vs damping coefficient
for a given component mass
'''

import damper as d
import matplotlib.pyplot as plt
import numpy as np

# acceleration values to plot over
g = 9.81
a_min = 0.5 * g # m / s^2
a_avg = g
a_max = 1.5 * g
a_vals = [a_min, a_avg, a_max]

# range of damping constants
c_min = 1.0 # kN * s / m
c_max = 10.0
c_vals = np.linspace(c_min, c_max)

# other constants
dt = 0.1 # sec
m = 907 # kg
f_max = 4.0 # kN
damp = d.Damper(0.0, 1.0, f_max)
sys = d.System(m, damp)

# plot reduction vs c for all values of a_s
accum = []
for a in a_vals:
    for c in c_vals:
        # update C and add reduction to accumulator
        sys.damper.coef = c
        new_val = sys.reduction(a, dt)
        accum = accum + [new_val]
    # plot and reset accumulator for next acceleration
    plt.plot(c_vals, accum)
    accum = []
plt.show()
