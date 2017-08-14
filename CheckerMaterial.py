import math
import Color as col
class CheckerMaterial():
    def __init__(self, scale, reflectiveness):
        self.scale = scale
        self.reflectiveness = reflectiveness

    def sample(self, ray, position, normal):
        return col.black if \
            abs((math.floor(position.x * self.scale) + math.floor(position.z * self.scale)) % 2 ) < 1 else col.white
