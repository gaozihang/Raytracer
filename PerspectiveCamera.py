from Vector3 import Vector3
from Ray3 import Ray3
import math
#right handed corrdinate system
class PerspectiveCamera():
    def __init__(self, eye, front, up, fov):
        self.eye = eye
        self.front = front
        self.fov = fov
        self.refUp = up

    def initialize(self):
        self.right = self.front.cross(self.refUp)
        self.up = self.right.cross(self.front)
        self.fovScale = math.tan(self.fov * 0.5 * math.pi / 180) * 2

    def generateRay(self, x, y):
        r = self.right.multiply((x - 0.5) * self.fovScale)
        u = self.up.multiply((y - 0.5) * self.fovScale)
        return Ray3(self.eye, self.front.add(r).add(u).normalize())
