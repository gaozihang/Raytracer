class Color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def copy(self):
        return Color(self.r, self.g, self.b)

    def add(self, c):
        return Color(self.r + c.r, self.g + c.g, self.b + c.b)

    def multiply(self, s):
        return Color(self.r * s, self.g * s, self.b * s)

    def modulate(self, c):
        return Color(self.r * c.r, self.g * c.g, self.b * c.b)

black = Color(0 ,0, 0)
white = Color(1 ,1, 1)
red = Color(1, 0, 0)
green = Color(0, 1, 0)
blue = Color(0, 0, 1)
