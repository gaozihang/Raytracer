from Ray3 import Ray3
from IntersectResult import IntersectResult
import IntersectResult as IR
import math
# \\x - c\\ = r, c is center, r is radius
# v = o -c
# minimum distance between the ray and sphere
# t = -d * v - sqrt((d * v) * (d * v) - (v * v - r * r))

class Sphere():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def initialize(self):
        self.sqrRadius = self.radius * self.radius

    def copy(self):
        return Sphere(self.center, self.radius)

    def intersect(self, ray):
        v = ray.origin.subtract(self.center)
        a0 = v.sqrLength() - self.sqrRadius
        DdotV = ray.direction.dot(v)

        if DdotV <= 0:
            discr = DdotV * DdotV - a0
            if discr >= 0:
                result = IntersectResult()
                result.geometry = self
                result.distance = - DdotV - math.sqrt(discr)
                result.position = ray.getPoint(result.distance)
                result.normal = result.position.subtract(self.center).normalize()
                return result
        # IntersectResult().geometry is None, means noHit
        return  IR.noHit
