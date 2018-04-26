class Account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def get_balance(self):
        a = self.balance
        # a *= 100
        # a += .5
        # a = int(a)
        # a /= 100
        return a

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def deposit(self, money):
        if money > 0:
            self.balance += money
            return True
        return False

    def withdraw(self, money):
        if self.get_balance() >= money > 0:
            self.balance -= money
            return True
        return False

    def __str__(self):
        a = self.get_balance()
        return '${:.2f}'.format(self.get_balance())
        # old way (works in python 2.7)
        # return '$%.2f' % self.get_balance()

    def __add__(self, other):
        name = self.get_name() + ' and ' + other.get_name()
        number = self.get_number() + other.get_number()
        balance = self.get_balance() + other.get_balance()
        return Account(name, number, balance)


if __name__ == '__main__':
    a = Account('John', 12345, 1500.00)
    print(a.get_balance())
    print('bad deposit', a.deposit(-50))
    print(a.get_balance())
    print('bad deposit', a.deposit(0))
    print(a.get_balance())
    print('good deposit', a.deposit(100))
    print(a.get_balance())

