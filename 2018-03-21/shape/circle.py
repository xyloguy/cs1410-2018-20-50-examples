import math

import pygame
import shape


class Circle(shape.Shape):
    def __init__(self, x, y, radius, color):
        shape.Shape.__init__(self, x, y, color)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.get_radius() ** 2

    def get_circumference(self):
        return 2 * math.pi * self.get_radius()

    def draw(self, surface):
        color = self.get_color()
        pos = (self.get_x(), self.get_y())
        radius = self.get_radius()
        pygame.draw.circle(surface, color, pos, radius)
