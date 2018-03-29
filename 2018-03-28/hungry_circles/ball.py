import random
import pygame
import math


class Ball:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height

        self.alive = True

        self.radius = random.randint(15, 30)
        self.x = random.randint(self.radius, self.width - self.radius)
        self.y = random.randint(self.radius, self.height - self.radius)

        red = random.randint(100, 255)
        green = random.randint(100, 255)
        blue = random.randint(100, 255)
        self.color = (red, green, blue)

        self.dx = random.randint(25, 100) * random.choice([1, -1])
        self.dy = random.randint(25, 100) * random.choice([1, -1])

    def move(self, dt):
        if not self.alive:
            return

        dx = dt * self.dx
        dy = dt * self.dy

        self.x += dx
        if self.x + self.radius >= self.width:
            self.x = self.width - self.radius
            self.dx *= -1
        elif self.x - self.radius <= 0:
            self.x = 0 + self.radius
            self.dx *= -1

        self.y += dy
        if self.y + self.radius >= self.height:
            self.y = self.height - self.radius
            self.dy *= -1
        elif self.y - self.radius <= 0:
            self.y = 0 + self.radius
            self.dy *= -1

    def hits(self, other):
        if not self.alive or not other.alive:
            return False

        x1 = self.x
        y1 = self.y
        r1 = self.radius

        x2 = other.x
        y2 = other.y
        r2 = other.radius

        min_distance = r1 + r2
        actual_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return actual_distance <= min_distance

    def __gt__(self, other):
        return self.radius > other.radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def __iadd__(self, other):
        other.alive = False
        area = self.get_area() + other.get_area()
        self.radius = int(math.ceil(math.sqrt(area / math.pi)))

        r1, g1, b1 = self.color
        r2, g2, b2 = other.color

        red = (r1 + r2) / 2
        green = (g1 + g2) / 2
        blue = (b1 + b2) / 2
        self.color = (red, green, blue)

        return self

    def draw(self, surface):
        if not self.alive:
            return
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)