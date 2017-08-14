import math
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def copy(self):
        return Vector3(self.x, self.y, self.z)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def sqrLength(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def normalize(self):
        inv = 1 / self.length()
        return Vector3(self.x * inv, self.y * inv, self.z * inv)

    def negate(self):
        return Vector3(-self.x, -self.y, -self.z)

    def add(self, v):
        return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

    def subtract(self, v):
        return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)

    def multiply(self, f):
        return Vector3(self.x * f, self.y * f, self.z * f)

    def divide(self, f):
        invf = 1 / f
        return Vector3(self.x * invf, self.y * invf, self.z * invf)

    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self, v):
        return Vector3(-self.z * v.y + self.y * v.z, self.z * v.x - self.x * v.z, -self.y * v.x + self.x * v.y )

zero = Vector3(0, 0, 0)