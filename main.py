from PIL import Image, ImageDraw
import random
from Sphere import Sphere
from CheckerMaterial import CheckerMaterial
from PerspectiveCamera import PerspectiveCamera
from Vector3 import Vector3
from Plane import Plane
from Ray3 import Ray3
from PhongMaterial import PhongMaterial
from Union import Union
import Color as col

def rayTraceRecursive(scene, ray, maxReflect):
    result = scene.intersect(ray)

    if result.geometry:
        reflectiveness = result.geometry.material.reflectiveness
        color = result.geometry.material.sample(ray, result.position, result.normal)
        color = color.multiply(1 - reflectiveness)

        if reflectiveness > 0 and maxReflect > 0:
            r = result.normal.multiply(-2 * result.normal.dot(ray.direction)).add(ray.direction)
            ray = Ray3(result.position, r)
            reflectedColor = rayTraceRecursive(scene, ray, maxReflect - 1)
            color = color.add(reflectedColor.multiply(reflectiveness))
        return color
    else:
        return col.black

w = 400
h = 400
im = Image.new('RGBA', (w, h), (0, 0, 0, 255))
draw = ImageDraw.Draw(im)

plane = Plane(Vector3(0, 1, 0), 0)
plane.material = CheckerMaterial(0.1, 0.5)
sphere1 = Sphere(Vector3(-10, 10, -10), 10)
sphere2 = Sphere(Vector3(10, 10, -10), 10)
sphere1.material = PhongMaterial(col.red, col.white, 16, 0.25)
sphere2.material = PhongMaterial(col.blue, col.white, 16, 0.25)
camera = PerspectiveCamera(Vector3(0, 5, 15), Vector3(0, 0, -1), Vector3(0, 1, 0), 90)

sphere1.initialize()
sphere2.initialize()
camera.initialize()

union = Union([plane, sphere1, sphere2])

for y in range(0, h):
    sy = 1 - y / h
    for x in  range(0, w):
        sx = x / w
        ray = camera.generateRay(sx, sy)
        result = union.intersect(ray)
        color = rayTraceRecursive(union, ray, 3)
        draw.point((x, y), fill=(int(color.r * 255), int(color.g * 255), int(color.b * 255), 255))
im.show()
im.save('out.png','png')