from math import cos, sin, pi

class Line:
    '''Line'''
    def __init__(self, pta, ptb):
        self.pta = int(pta[0]), int(pta[1])
        self.ptb = int(ptb[0]), int(ptb[1])

    def __repr__(self):
        return 'Line '+str(self.pta)+', '+str(self.ptb)

    @classmethod
    def from_rotation(cls, pta, rotation, magnitude):
        '''Create line, basing on its rotation and magnitude
        Copied from Vector
        '''
        obj = cls.__new__(cls)
        xratio = cos(obj.to_rads(rotation))
        yratio = sin(obj.to_rads(rotation))
        xdelta, ydelta = xratio * magnitude, yratio * magnitude
        obj.pta = int(pta[0]), int(pta[1])
        obj.ptb = int(xdelta+pta[0]), int(ydelta+pta[1])
        return obj

    # Helper methods

    @staticmethod
    def to_rads(degs):
        return (2*pi*degs)/360

    @staticmethod
    def to_degs(rads):
        return (360*rads)/(2*pi)


class Circle:
    '''Circle'''
    def __init__(self, center, radius, slice=None):
        self.center, self.radius = center, radius
        self.slice = slice
