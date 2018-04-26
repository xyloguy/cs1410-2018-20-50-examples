from unittest import TestCase, main
from account import Account
from checking_account import CheckingAccount


class CheckingAccountTestCase(TestCase):
    def test_create_checking_account(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        overdraft = 100
        a = CheckingAccount(name, number, balance, overdraft)
        self.assertIsInstance(a, CheckingAccount)
        self.assertIsInstance(a, Account)

    def test_create_checking_verify_overdraft_limit(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        overdraft = 100
        a = CheckingAccount(name, number, balance, overdraft)
        self.assertEqual(overdraft, a.get_overdraft())

    def test_withdraw_fail_negative_money(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        overdraft = 100
        a = CheckingAccount(name, number, balance, overdraft)
        self.assertFalse(a.withdraw(-500))
        self.assertEqual(balance, a.get_balance())

    def test_withdraw_fail_zero_money(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        overdraft = 100
        a = CheckingAccount(name, number, balance, overdraft)
        self.assertFalse(a.withdraw(0))
        self.assertEqual(balance, a.get_balance())

    def test_withdraw_fail_not_enough_money(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        overdraft = 100
        a = CheckingAccount(name, number, balance, overdraft)
        self.assertFalse(a.withdraw(balance + 100.01))
        self.assertEqual(balance, a.get_balance())

    def test_withdraw_success_01(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        overdraft = 100
        a = CheckingAccount(name, number, balance, overdraft)
        self.assertTrue(a.withdraw(balance + 100))
        self.assertEqual(-100, a.get_balance())

    def test_withdraw_success_02(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        overdraft = 100
        a = CheckingAccount(name, number, balance, overdraft)
        self.assertTrue(a.withdraw(0.01))
        self.assertEqual(balance - 0.01, a.get_balance())

    def test_withdraw_success_03(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        overdraft = 100
        a = CheckingAccount(name, number, balance, overdraft)
        self.assertTrue(a.withdraw(balance + 25.56))
        self.assertAlmostEqual(-25.56, a.get_balance(), 2)


if __name__ == '__main__':
    main()