class BankAccount:
    # constructor
    def __init__(self, name, starting_balance):
        self.owner = name
        self.balance = starting_balance

    # deposit
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    # withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    # get balance
    def get_balance(self):
        return self.balance

    # get owner
    def get_owner(self):
        return self.owner


class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn
        self.addresses = []
        self.phones = []

    def add_address(self, address):
        self.addresses.append(address)

    def add_phone(self, phone):
        self.phones.append(phone)

    def __str__(self):
        return 'Name: {}, SSN: {}'.format(self.name, self.ssn)


class Address:
    def __init__(self, *args):
        self.lines = args

    def __str__(self):
        s = ''
        for line in self.lines:
            s += str(line)
            s += '\n'
        return s.strip()


jane = Person('Jane Doe', '999-99-9999')
b = BankAccount(jane, 1000)
print(b.get_balance())
print(b.get_owner())
b.deposit(-1000)
print(b.get_balance())
b.deposit(200)
print(b.get_balance())
b.withdraw(100)
#b.owner.name = 'Jane Smith'
jane.name = 'Jane Smith'

a = Address('123 Fake St.', 'Somewhere', 'MT', 99999, 'USA')

jane.add_address(a)
print(a)
jane.add_phone('555-555-5555')
print(b.get_balance())
b.withdraw(-100)
print(b.get_balance())
b.withdraw(1100.01)
print(b.get_balance())
print(b.get_owner())