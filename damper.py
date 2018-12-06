from __future__ import division

class Damper:
    '''
    represents a viscous damper in terms of damping coefficient and exponent.
    '''
    def __init__(self, C, a, f_max):
        '''
        creates an instance of a damper class
        C: damping coefficient (kN * s / m)
        a: alpha value
        f_max: max output force of damper (kN)
        '''
        self.coef = C
        self.alpha = a
        self.fMax = f_max
    def force(self, v):
        '''
        damping force at a given velocity
        v: relative velocity (m / s)
        '''
        C = self.coef
        a = self.alpha
        f_max = self.fMax
        force_out = C * (v ** a)
        return min([f_max, force_out])

class Shockwave:
    '''
    shockwave from earthquake, represents seismic load.
    '''
    def __init__(self, a, dt):
        '''
        creates an instance of Shockwave.
        a: acceleration of component from wave (m / s^2)
        dt: peak to peak time (s)
        '''
        self.accel = a
        self.ptp = dt

class System:
    '''
    system with a mass connected to a viscous damper along the axis of motion subjected to a seismic wave.
    '''
    def __init__(self, m, damp, wave):
        '''
        creates an instance of System.
        m: mass of component (kg)
        damp: instance of Damper
        '''
        self.mass = m
        self.damper = damp
        self.wave = wave
    def compAccel(self):
        '''
        acceleration of component. (m/s^2)
        '''
        a = self.wave.accel
        dt = self.wave.ptp
        v = a * dt
        f = self.damper.force(v) * 1000
        m = self.mass
        return a - (f / m)
    def reduction(self):
        '''
        percent reduction of acceleration from damper.
        wave: input from earthquake
        '''
        a = self.compAccel()
        a_s = self.wave.accel
        return 100 - (a / a_s * 100)
