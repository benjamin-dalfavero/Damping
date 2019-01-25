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

