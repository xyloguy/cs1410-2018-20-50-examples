class Marker:
    def __init__(self, color):
        self.color = color
        self.ink = 10
        self.tipsize = .01
        self.erasable = True

    def write(self, length):
        self.ink -= self.tipsize * abs(length)
        if self.ink <= 0:
            self.ink = 0

    def print(self):
        print(self.color, self.ink, self.tipsize, self.erasable)
