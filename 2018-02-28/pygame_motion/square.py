import pygame

class Square:
    def __init__(self, swidth, sheight, x, y, size, color, dx, dy):
        self.screen_width = swidth
        self.screen_height = sheight
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.dx = dx
        self.dy = dy

    def evolve(self, dt):
        newx = self.x + (self.dx * dt)
        newy = self.y + (self.dy * dt)

        if newx < 0 or (newx + self.size) > self.screen_width:
            self.dx *= -1

        if newy < 0 or (newy + self.size) > self.screen_height:
            self.dy *= -1

        self.x = newx
        self.y = newy
        return

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(surface, self.color, rect)

