class Person:
    def __init__(self, name):
        self.name = name
        self.mom = None
        self.dad = None

    def addMom(self, mom):
        self.mom = mom

    def addDad(self, dad):
        self.dad = dad

    def __str__(self):
        s = self.name

        if self.mom is not None:
            s += ', Mom: ' + str(self.mom)

        if self.dad is not None:
            s += ', Dad: ' + str(self.dad)

        return s


julie = Person('Julie')
print(julie)
jim = Person('Jim')

susan = Person('Susan')
jim.addMom(susan)
print(jim)

mark = Person('Mark')
mark.addMom(julie)
mark.addDad(jim)
print(mark)

debbie = Person('Debbie')
debbie.addMom(julie)
debbie.addDad(jim)



