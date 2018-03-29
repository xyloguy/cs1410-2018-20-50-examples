from math import pi, sqrt


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return pi * self.get_radius() ** 2

    def get_circumference(self):
        return 2 * pi * self.get_radius()

    def get_radius_from_area(self, area):
        return sqrt(area / pi)

    def set_radius_from_area(self, area):
        self.set_radius(self.get_radius_from_area(area))

    def add_circle(self, other):
        return self + other

    def __add__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()
        new_area = a1 + a2
        new_radius = self.get_radius_from_area(new_area)
        return Circle(new_radius)

    def __gt__(self, other):
        r1 = self.get_radius()
        r2 = other.get_radius()
        return r1 > r2

    def __lt__(self, other):
        return other > self

    def __eq__(self, other):
        return not self > other and not self < other

    def __ne__(self, other):
        return not self == other

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return not self > other

    def __iadd__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()
        new_area = a1 + a2
        self.set_radius_from_area(new_area)
        return self


if __name__ == '__main__':
    c = Circle(3)
    b = Circle(2)
    a = b + c
    print('c', c.get_radius(), c.get_area())
    print('b', b.get_radius(), b.get_area())
    print('a', a.get_radius(), a.get_area())

    a = c.add_circle(b)

    print(b > c)
    print(b <= c)
    print(b < c)
    print(b == c)
    print(b != c)

    c += b
    print('c', c.get_radius(), c.get_area())

