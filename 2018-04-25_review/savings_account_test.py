from unittest import TestCase, main
from account import Account
from savings_account import SavingsAccount


class SavingsAccountTestCase(TestCase):
    def test_create_account(self):
        name = 'Jaime'
        number = 6732
        balance = 10000
        interest = 0.01
        a = SavingsAccount(name, number, balance, interest)
        self.assertIsInstance(a, SavingsAccount)
        self.assertIsInstance(a, Account)

    def test_create_account_interest_rate(self):
        name = 'Jaime'
        number = 6732
        balance = 10000
        interest = 0.01
        a = SavingsAccount(name, number, balance, interest)
        self.assertEqual(interest, a.get_interest_rate())

    def test_compound_interest(self):
        name = 'Jaime'
        number = 6732
        balance = 10000
        interest = 0.01
        a = SavingsAccount(name, number, balance, interest)

        m_rate = interest / 12
        added = balance * m_rate
        new_balance = added + balance

        self.assertEqual(added, a.compound_interest())
        self.assertEqual(new_balance, a.get_balance())



if __name__ == '__main__':
    main()