class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def speak(self):
        raise NotImplementedError
