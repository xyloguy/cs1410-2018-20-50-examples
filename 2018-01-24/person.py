class Person:
    def __init__(self, name, age, height, weight, gender):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

    def print(self):
        string = 'Name: ' + self.name + ', Basal Metabolic Rate: ' + str(self.get_bmr())
        return string

    def get_bmr(self):
        if self.gender == 'm':
            return 66 + (12.7 * self.height) + (6.23 * self.weight) - (6.8 * self.age)
        else:
            return 655 + (4.7 * self.height) + (4.35 * self.weight) - (4.7 * self.age)


john = Person('John Doe', 35, 72, 225, 'm')
jane = Person('Jane Smith', 23, 65, 135, 'f')

print(john.print())
print(jane.print())