import rect
import mountain

class House:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.walls = rect.Rect(x + width//6, y + height//3, width//3*2, height//3*2, (224,204,74))
        self.roof = mountain.Mountain(x + width//2, y, width, y + height//3, (0, 0, 0))
    def draw(self, surface):
        self.walls.draw(surface)
        self.roof.draw(surface)