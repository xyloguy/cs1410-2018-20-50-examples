import rectangle


class Square(rectangle.Rectangle):
    def __init__(self, x, y, size, color):
        rectangle.Rectangle.__init__(self, x, y, size, size, color)

    def get_size(self):
        return self.get_width()

    def set_size(self, size):
        rectangle.Rectangle.set_width(self, size)
        rectangle.Rectangle.set_height(self, size)

    def set_width(self, size):
        self.set_size(size)

    def set_height(self, size):
        self.set_size(size)


s = Square(5, 20, 10, 'red')
s.set_y(19)
s.set_width(7)
s.set_size(20)
s.set_height(10)
print(s.get_area())