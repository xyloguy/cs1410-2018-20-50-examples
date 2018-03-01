import pygame
import square
import circle
import random


class New:
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height

        self.squares = []
        classes = [
            square.Square,
            circle.Circle,
        ]
        for i in range(15):
            size = random.randint(5, 100)
            x = random.randint(0, width - size)
            y = random.randint(0, height - size)
            r = random.randint(100, 255)
            g = random.randint(100, 255)
            b = random.randint(100, 255)
            color = (r, g, b)
            dx = random.randint(-200, 200)
            dy = random.randint(-200, 200)
            obj = random.choice(classes)

            s = obj(width, height, x, y, size, color, dx, dy)
            self.squares.append(s)

        return

    # move the circles down every frame according to how much time has passed
    # don't let the circles go off the window
    def evolve(self, dt):

        for s in self.squares:
            s.evolve(dt)

        return

    # draws the current state of the system
    def draw(self, surface):
        surface.fill((0, 0, 0))

        for s in self.squares:
            s.draw(surface)

        return
