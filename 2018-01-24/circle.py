from math import pi

class Circle:
    def __init__(self, radius):
        self.mRadius = radius

    def getRadius(self):
        return self.mRadius

    def getDiameter(self):
        return 2 * self.getRadius()

    def calculateArea(self):
        return pi * self.getRadius()**2

    def calculateCircumference(self):
        return self.getDiameter() * pi


c = Circle(10)
print(c.getRadius()) # 10
print(c.getDiameter()) # 20
print(c.calculateArea()) # 314.16
print(c.calculateCircumference()) # 62.8
