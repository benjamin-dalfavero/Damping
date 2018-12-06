'''
plot reduction of acceleration vs damping coefficient
for a given component mass
'''

import damper as d
import matplotlib.pyplot as plt
import numpy as np

def plotCVals(shock, sys, cs):
    '''
    plot reduction efficiency for various values of C
    when subjected to a shockwave, and with a component of
    a certain mass.
    shock: (acceleration, ptp time)
    sys: Damper.System
    cs: range of values for c
    '''
    a, dt = shock
    # basically a map of reduction over values of c
    accum = []
    for c in cs:
        sys.damper.coef = c
        accum += [sys.reduction(a, dt)]
    plt.plot(cs, accum)
