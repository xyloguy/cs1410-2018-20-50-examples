import shape
import pygame


class Rectangle(shape.Shape):
    def __init__(self, x, y, width, height, color):
        shape.Shape.__init__(self, x, y, color)
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return 2 * self.get_width() + 2 * self.get_height()

    def draw(self, surface):
        rect = pygame.Rect(
            self.get_x(),
            self.get_y(),
            self.get_width(),
            self.get_height()
        )
        pygame.draw.rect(surface, self.get_color(), rect)
