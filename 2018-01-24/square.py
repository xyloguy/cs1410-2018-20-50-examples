class Square:
    def __init__(self, size):
        self.__size = size

    def getSize(self):
        return self.__size

    def getWidth(self):
        return self.getSize()

    def getHeight(self):
        return self.getSize()

    def calculateArea(self):
        return self.getSize()**2

    def calculatePerimeter(self):
        return self.getSize() * 4


r = Square(20)
print(r.getWidth()) #20
print(r.getHeight()) #20
print(r.calculateArea()) #400
print(r.calculatePerimeter()) #80