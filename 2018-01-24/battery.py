class Battery:
    def __init__(self, capacity, rechargable):
        self.capacity = capacity
        self.maxcapacity = capacity
        self.rechargable = rechargable

    def discharge(self, amount):
        if amount < 0:
            return
        self.capacity -= amount
        if self.capacity < 0:
            self.capacity = 0

    def charge(self, amount):
        if amount < 0 or not self.rechargable:
            return
        self.capacity += amount
        if self.capacity > self.maxcapacity:
            self.capacity = self.maxcapacity

