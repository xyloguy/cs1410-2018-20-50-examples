from account import Account


class SavingsAccount(Account):
    def __init__(self, name, number, balance, interest_rate):
        Account.__init__(self, name, number, balance)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def compound_interest(self):
        m_rate = self.get_interest_rate() / 12
        added = self.get_balance() * m_rate
        self.balance += added
        return added