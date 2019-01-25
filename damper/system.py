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

