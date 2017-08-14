import Vector3
from Vector3 import Vector3
import Color as col
import math

class PhongMaterial():
    def __init__(self, diffuse, specular, shininess, reflectiveness):
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.reflectiveness = reflectiveness

    def sample(self, ray, position, normal):
        NdotL = normal.dot(lightDir)
        # Blinn-phong
        H = lightDir.subtract(ray.direction).normalize()
        NdotH = normal.dot(H)

        # phong
        # R = normal.multiply(lightDir.multiply(2).dot(normal)).subtract(lightDir)
        # V = ray.direction.negate()
        # RdotV = R.dot(V)
        # specularTerm = self.specular.multiply(math.pow(max(RdotV, 0), self.shininess))

        diffuseTerm = self.diffuse.multiply(max(NdotL, 0))
        specularTerm = self.specular.multiply(math.pow(max(NdotH, 0), self.shininess))
        return lighrColor.modulate(diffuseTerm.add(specularTerm))

# global light
lightDir = Vector3(1, 1, 1).normalize()
lighrColor = col.white