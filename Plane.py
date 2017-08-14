from Vector3 import Vector3
from IntersectResult import IntersectResult
import IntersectResult as IR
# n * x = d
class Plane():
    def __init__(self, normal, d):
        self.normal = normal
        self.d = d

    def initialize(self):
        self.position = self.normal.multiply(self.d)

    def intersect(self, ray):
        a = ray.direction.dot(self.normal)
        if a >= 0:
            return IR.noHit

        b = self.normal.dot(ray.origin.subtract(self.position))
        result = IntersectResult()
        result.geometry = self
        result.distance = - b / a
        result.position = ray.getPoint(result.distance)
        result.normal = self.normal
        return result