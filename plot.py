import damper as d
import matplotlib.pyplot as plt
import numpy as np

def mapCs(sys, cs):
    # map reduction over values of c
    old_c = sys.damper.coef
    accum = []
    for c in cs:
        sys.damper.coef = c
        accum.append(sys.force_ratio())
    sys.damper.coef = old_c
    return accum

def plotCase(name, sys, c_vals, a_vals):
    # plot force ratio vs c for all values of a
    for a in a_vals:
        sys.wave.accel = a
        force_vals = mapCs(sys, c_vals)
        plt.plot(c_vals, force_vals)
    # put titles on graph
    plt.title(name)
    plt.xlabel('C')
    plt.ylabel('Force Ratio')
    filename = name.replace(' ', '_') + ".jpg"
    plt.savefig(filename)
    plt.clf()

# define test cases

# acceleration values
g = 9.81
a_vals = [0.5 * g, g, 1.5 * g]
shockwave = d.Shockwave(4.905, 0.2)

# C values based on range in catalog.
# mass chosen to fit approximately with ideal range of damper.

ld500 = d.Damper(6.55, 1.0, 4.0)
ld500_sys = d.System(907.18, ld500, shockwave)
ld500_c_vals = np.arange(1.0, 10.0, 0.01)

ld700 = d.Damper(16.5, 1.0, 10)
ld700_sys = d.System(1361, ld700, shockwave)
ld700_c_vals = np.arange(3.0, 20.0, 0.01)

# plot
plotCase("LD500 2000lbs", ld500_sys, ld500_c_vals, a_vals)
plotCase("LD700 3000lbs", ld700_sys, ld700_c_vals, a_vals)