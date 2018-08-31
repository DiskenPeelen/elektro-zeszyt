from math import sqrt
import numpy as np
from PIL import Image as PilImage # for saving
from src.shapes import Line, Circle
from src.vector import Vector2D as Vector

dtype = np.uint8
to_color = lambda x: np.array(x, dtype=dtype)

class Image:
    def __init__(self, size, line_width=1.5, vector_arrow_relative=False,
            vector_arrow_size=10):
        self.size = size
        self.pixels = to_color(np.ones((size[1], size[0], 3))*255)
        self.vector_arrow_relative = vector_arrow_relative
        self.vector_arrow_size = vector_arrow_size
        self.linew = line_width

    def save(self, path):
        pillow = PilImage.fromarray(np.uint8(self.pixels))
        pillow.save(path)

    def draw_point(self, point, fill=[0,0,0], width=None):
        '''Draw a point'''
        if width == None: width = self.linew
        fill = to_color(fill)
        min_x = point[0] - width
        max_x = point[0] + width
        min_y = point[1] - width
        max_y = point[1] + width
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                dist = self.ptdist((x,y), point)
                if dist <= width:
                    try: self.pixels[y, x] = fill
                    except IndexError: pass

    def draw_circle(self, circle, fill=[0,0,0], width=None):
        '''Draw a circle'''
        if width == None: width = self.linew
        fill = to_color(fill)
        outer_radius = circle.radius
        inner_radius = circle.radius - width
        min_x = circle.center[0] - outer_radius
        max_x = circle.center[0] + outer_radius
        min_y = circle.center[1] - outer_radius
        max_y = circle.center[1] + outer_radius
        if circle.slice == None:
            for y in range(min_y, max_y+1):
                for x in range(min_x, max_x+1):
                    dist = self.ptdist((x,y), circle.center)
                    if dist > inner_radius and dist <= outer_radius:
                        try: self.pixels[y, x] = fill
                        except IndexError: pass
        else:
            for slice_open, slice_close, slice_reversed in circle.slice:
                for y in range(min_y, max_y+1):
                    for x in range(min_x, max_x+1):
                        vector = Vector.from_absolute(circle.center, (x,y))
                        angle = vector.angle
                        dist = vector.magnitude
                        if not(dist > inner_radius and dist <= outer_radius):
                            continue
                        if slice_reversed:
                            if angle < slice_open or angle > slice_close:
                                try: self.pixels[y, x] = fill
                                except IndexError: pass
                        else:
                            if angle > slice_open and angle < slice_close:
                                try: self.pixels[y, x] = fill
                                except IndexError: pass

    def draw_line(self, line, fill=to_color([0,0,0]), width=None):
        '''Draw a line'''
        if width == None: width = self.linew
        pta, ptb = line.pta, line.ptb
        min_x, max_x = min([pta[0], ptb[0]]), max([pta[0], ptb[0]])
        min_y, max_y = min([pta[1], ptb[1]]), max([pta[1], ptb[1]])
        for y in range(min_y-width, max_y+1+width):
            for x in range(min_x-width, max_x+1+width):
                dist = self.lndist(pta, ptb, (x,y))
                if dist <= width:
                    try: self.pixels[y, x] = fill
                    except IndexError: pass


    def draw_vector(self, vector, fill=to_color([0,0,0]), width=None):
        '''Draw a vector'''
        if width == None: width = self.linew
        arrow_angle = 180-35 # angle between vector and arrow arm [degs]
        ipt, tpt, angle = vector.init_pt, vector.term_pt, vector.angle
        alen = self.vector_arrow_size
        if self.vector_arrow_relative:
            alen *= vector.magnitude
        base_angle = vector.angle + 90
        self.draw_line(Line(ipt, tpt))
        self.draw_line(Line.from_rotation(tpt, base_angle+arrow_angle, alen))
        self.draw_line(Line.from_rotation(tpt, base_angle-arrow_angle, alen))


    @staticmethod
    def lndist(lpta, lptb, pt):
        '''Distance between point and a line which is defined by 2 other pts'''
        x0, y0 = pt
        x1, y1 = lpta
        x2, y2 = lptb
        dist = abs(x0*(y2-y1) - y0*(x2-x1) + x2*y1 - y2*x1)
        dist /= sqrt((y2-y1)**2 + (x2-x1)**2)
        return dist

    @staticmethod
    def ptdist(pta, ptb):
        '''Distance between points'''
        xa, ya = pta
        xb, yb = ptb
        xdiff = abs(xa - xb)
        ydiff = abs(ya - yb)
        return sqrt(pow(xdiff, 2) + pow(ydiff, 2))
