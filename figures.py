
from mathLib import *

class Sphere(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def ray_intersect(self, orig, dir):
        L = subtractVectors(self.center, orig)
        
        tca = dotProduct(L, dir)
        d = (norm(L) ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return False

        thc = (self.radius ** 2 - d ** 2) ** 0.5

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return False
        
        return True
