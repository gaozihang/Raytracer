import Vector3
class IntersectResult():
    def __init__(self):
        self.geometry = None
        self.distance = 0
        self.position = Vector3.zero
        self.normal = Vector3.zero

noHit = IntersectResult()
