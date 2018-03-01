import pygame

class Mountain:
    def __init__(self, x, y, width, bottom, color):
        self.points = [(x, y), (x+width//2, bottom), (x-width//2, bottom)]
        self.color = color

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.points)
