from account import Account


class CheckingAccount(Account):
    def __init__(self, name, number, balance, overdraft_limit):
        Account.__init__(self, name, number, balance)
        self.overdraft_limit = overdraft_limit

    def get_overdraft(self):
        return self.overdraft_limit

    def withdraw(self, money):
        available_amount = self.get_balance() + self.get_overdraft()
        if available_amount >= money > 0:
            self.balance -= money
            return True
        return False
