from math import sqrt, atan, pi, cos, sin

class Vector2D:
    '''Class represents Euclidean Vector.
    Contains method for method usable on plane'''
    def __init__(self, init_pt, delta):
        '''Create a vector, basing on coords of its init point and delta'''
        self.init_pt = init_pt
        self.xdelta = delta[0]
        self.ydelta = delta[1]
        self.recalc()

    @classmethod
    def from_absolute(cls, init_pt, term_pt):
        '''Create vector, basing on absolude coords of its init and term pts'''
        obj = cls.__new__(cls)
        obj.init_pt = init_pt
        obj.term_pt = term_pt
        obj.xdelta = term_pt[0] - init_pt[0]
        obj.ydelta = term_pt[1] - init_pt[1]
        obj.recalc()
        return obj

    @classmethod
    def from_rotation(cls, init_pt, rotation, magnitude):
        '''Create vector, basing on its rotation and magnitude'''
        obj = cls.__new__(cls)
        xratio = cos(cls.to_rads(rotation))
        yratio = sin(cls.to_rads(rotation))
        obj.init_pt = init_pt
        obj.xdelta = xratio * magnitude
        obj.ydelta = yratio * magnitude
        obj.recalc()
        return obj

    @classmethod
    def from_reversed(cls, vector):
        '''Create vector, switch init and term pts of another one'''
        obj = cls.__new__(cls)
        vector.recalc()
        init_pt = vector.term_pt
        term_pt = vector.init_pt
        obj.init_pt = init_pt
        obj.xdelta = term_pt[0] - init_pt[0]
        obj.ydelta = term_pt[1] - init_pt[1]
        obj.recalc()
        return obj

    def __repr__(self):
        '''Generate repr string of the Vector'''
        return 'Vector '+str([self.xdelta, self.ydelta]) + \
            '\t(rotation='+str(round(self.angle)) + \
            ',\tmagn='+str(round(self.magnitude, 2))+')'

    def recalc(self):
        '''Recalculate magnitude and angle of the Vector
        Additionally calculate abosule position of terminal point
        '''
        self.magnitude = sqrt(self.xdelta**2 + self.ydelta**2)
        try: slope = self.xdelta / self.ydelta
        except ZeroDivisionError:
            if self.xdelta < 0: slope = float('inf')
            elif self.xdelta > 0: slope = -float('inf')
            else: slope = 0
        deg = 360*atan(slope)/(2*pi)
        if self.xdelta < 0 and self.ydelta > 0: deg = 180 - abs(deg)
        if self.xdelta > 0 and self.ydelta > 0: deg = 180 + abs(deg)
        if self.xdelta == 0 and self.ydelta > 0: deg += 180
        deg += 90
        if self.xdelta == 0 and self.ydelta == 0: deg = 0
        self.angle = (270+(360-deg))%360
        self.term_pt = self.xdelta+self.init_pt[0], self.ydelta+self.init_pt[1]

    def get(self):
        return self.xdelta, self.ydelta

    def round(self, positions=0):
        '''Round vector's values to intigers or $ positions after comma'''
        self.xdelta = round(self.xdelta, positions)
        self.ydelta = round(self.ydelta, positions)
        self.recalc()

    def scale(self, scalar):
        '''Scale vector by some value'''
        self.xdelta = self.xdelta*scalar
        self.ydelta = self.ydelta*scalar
        self.recalc()

    # Helper methods

    @staticmethod
    def to_rads(degs):
        return (2*pi*degs)/360

    @staticmethod
    def to_degs(rads):
        return (360*rads)/(2*pi)
