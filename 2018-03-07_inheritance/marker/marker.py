class Marker:
    def __init__(self, color, capacity, tipsize, erasable):
        self.color = color
        self.cap = capacity
        self.tip = tipsize
        self.erasable = erasable
        self.owner = None

    def write(self):
        return 'I wrote'

    def set_owner(self, owner):
        self.owner = owner
