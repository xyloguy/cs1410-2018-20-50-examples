import pygame

class Circle:
    def __init__(self, swidth, sheight, x, y, size, color, dx, dy):
        size //= 2
        self.screen_width = swidth
        self.screen_height = sheight
        self.x = x
        if self.x - size <= 0:
            self.x = size
        self.y = y
        if self.y - size <= 0:
            self.y = size
        self.radius = size
        self.color = color
        self.dx = dx
        self.dy = dy

    def evolve(self, dt):
        newx = self.x + (self.dx * dt)
        newy = self.y + (self.dy * dt)

        if (newx - self.radius) < 0 or (newx + self.radius) > self.screen_width:
            self.dx *= -1

        if (newy - self.radius) < 0 or (newy + self.radius) > self.screen_height:
            self.dy *= -1

        self.x = newx
        self.y = newy
        return

    def draw(self, surface):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius)

