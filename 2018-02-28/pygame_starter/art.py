import pygame
import rect
import mountain
import house

class Art:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.sky = rect.Rect(0, 0, width, height, (20, 235, 250))
        self.grass = rect.Rect(0, 640, width, 320, (120, 190, 50))
        self.mountain1 = mountain.Mountain(200, 80, 640, 640, (50, 60, 160))
        self.mountain2 = mountain.Mountain(400, 120, 500, 640, (5, 15, 120))
        self.house = house.House(800, 540, 100, 100)
        self.house2 = house.House(850, 540, 150, 150)

    def evolve(self, dt):
        return

    def draw(self, surface):
        self.sky.draw(surface)

        self.mountain1.draw(surface)
        self.mountain2.draw(surface)

        self.grass.draw(surface)


        self.house.draw(surface)
        self.house2.draw(surface)


        return