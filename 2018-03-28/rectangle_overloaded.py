import math


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return self.get_width() * 2 + self.get_height() * 2

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __add__(self, other):
        total_area = self.get_area() + other.get_area()
        m = math.sqrt(total_area / self.get_area())
        new_width = self.get_width() * m
        new_height = self.get_height() * m
        return Rectangle(new_width, new_height)


if __name__ == '__main__':
    r1 = Rectangle(20, 10)
    r2 = Rectangle(2, 30)
    print(r1 > r2) # True
    r3 = r1 + r2
    print(r1.get_area() + r2.get_area())
    print(r3.get_width(), r3.get_height(), r3.get_area())