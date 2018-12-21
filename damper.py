from __future__ import division

'''
set of classes representing a viscously damped component under a seismic load
'''

class Damper:
    '''
    represents a viscous damper in terms of damping coefficient and exponent.
    '''
    def __init__(self, C, a, f_max):
        '''
        creates an instance of a damper class
        C: damping coefficient (kN*s/m)
        a: alpha value
        f_max: max output force of damper (kN)
        '''
        self.coef = C
        self.alpha = a
        self.f_max = f_max
    def force(self, v):
        '''
        damping force at a given velocity (kN)
        v: relative velocity (m/s)
        '''
        C = self.coef
        a = self.alpha
        force_out = C * (v ** a)
        return min([self.f_max, force_out])

class Shockwave:
    '''
    shockwave from earthquake, represents seismic load.
    '''
    def __init__(self, a, dt):
        '''
        creates an instance of Shockwave.
        a: acceleration of component from wave (m/s^2)
        dt: peak to peak time (s)
        '''
        self.accel = a
        self.ptp = dt
    def v_max(self):
        '''
        maximum velocity of wave (m/s)
        '''
        return self.accel * self.ptp

class System:
    '''
    system with a mass connected to a viscous damper along the axis of motion subjected to a seismic wave.
    '''
    def __init__(self, m, damp, wave):
        '''
        creates an instance of System.
        m: mass of component (kg)
        damp: instance of Damper
        wave: instace of Shockwave
        '''
        self.mass = m
        self.damper = damp
        self.wave = wave
    def comp_accel(self):
        '''
        acceleration of component. (m/s^2)
        '''
        a = self.wave.accel
        v = self.wave.v_max()
        f = self.damper.force(v) * 1000 # multiply because in kN
        m = self.mass
        return a - (f / m)
    def force_ratio(self):
        '''
        percent ratio of damping and seismic forces
        '''
        a = self.comp_accel()
        a_s = self.wave.accel
        return 100 - (a / a_s * 100)
