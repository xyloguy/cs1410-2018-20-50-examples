class Rectangle:
    def __init__(self, width, height):
        self.jsdfjsdfj = width
        self.__height = height

    def getWidth(self):
        return self.jsdfjsdfj

    def getHeight(self):
        return self.__height

    def calculateArea(self):
        return self.getWidth() * self.getHeight()
    
    def calculatePerimeter(self):
        return self.getWidth() * 2 + self.getHeight() * 2

r = Rectangle(10, 20)
print(r.getWidth()) #10
print(r.getHeight()) #20
print(r.calculateArea()) #200
print(r.calculatePerimeter()) #60