class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def set_x(self, x):
        old = self.get_x()
        if 0 <= x <= 500 and x != old:
            self.x = x
            return True
        return False

    def get_x(self):
        return self.x

    def set_y(self, y):
        old = self.get_y()
        if y >= 0 and y <= 500 and y != old:
            self.y = y
            return True
        return False

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color
