from Vector3 import Vector3

# r(t)= 0 + td, t >= 0, 0 is origin, d is direction

class Ray3():
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def getPoint(self, t):
        return self.origin.add(self.direction.multiply(t))

