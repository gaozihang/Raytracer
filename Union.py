import IntersectResult as IR
from Plane import Plane
from Sphere import Sphere

class Union():
    Infinity = 999999999
    def __init__(self, geometries):
        self.geometries = geometries
        for geometry in self.geometries:
            geometry.initialize()

    def intersect(self, ray):
        minDistance = self.Infinity
        minResult = IR.noHit

        for geometry in self.geometries:
            result = geometry.intersect(ray)
            if result.geometry and result.distance < minDistance:
                minDistance = result.distance
                minResult = result

        return minResult