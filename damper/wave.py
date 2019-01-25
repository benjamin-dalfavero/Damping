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

