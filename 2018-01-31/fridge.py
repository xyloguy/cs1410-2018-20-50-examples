class Fridge:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        remove = None
        if len(self.items) == self.capacity:
            remove = self.items[0]
            self.items = self.items[1:]
        self.items.append(item)
        return remove

f = Fridge(3)
print(f.add_item('eggs'))
print(f.add_item('milk'))
print(f.add_item('cheese'))
print(f.add_item('bacon'))
print(f.items)

