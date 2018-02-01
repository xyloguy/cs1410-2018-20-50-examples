import random


class Color:
    def __init__(self, r, g, b):
        v = 'p'
        self.red = r
        self.green = g
        self.blue = b

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue

    def set_red(self, new_value):
        if 0 <= new_value <= 255:
            self.red = new_value

    def set_green(self, new_value):
        if 0 <= new_value <= 255:
            self.green = new_value

    def set_blue(self, new_value):
        if 0 <= new_value <= 255:
            self.blue = new_value

    def string(self):
        # string concatenation
        return 'Color(' + str(self.get_red()) + ', ' + str(self.get_green()) + ', ' + str(self.get_blue()) + ')'

        r = self.get_red()
        g = self.get_green()
        b = self.get_blue()
        # string.format() (2.x, 3.x)
        # s = 'Color({}, {}, {})'
        # return s.format(r, g, b)

        # f strings (3.6+)
        # return f'Color({r}, {g}, {b})'

    def __str__(self):
        return self.string()

    def __repr__(self):
        return self.__str__()

c = Color(255, 0, 0)
print(c.get_blue())
c.set_blue(255)
print(c.get_blue())
print(c)
l = [c]
print(l)

for i in range(10):
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    c = Color(r, g, b)
    l.append(c)

print(len(l))
print(l)

b = Color(249, 222, 238)
