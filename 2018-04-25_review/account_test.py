from unittest import TestCase, main
from account import Account


class AccountTestCase(TestCase):
    def test_create_account(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertIsInstance(a, Account)
        self.assertEqual(name, a.get_name())
        self.assertEqual(number, a.get_number())
        self.assertEqual(balance, a.get_balance())

    def test_create_account_verify_name(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertEqual(name, a.get_name())

    def test_create_account_verify_acc_number(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertEqual(number, a.get_number())

    def test_create_account_verify_balance(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertEqual(balance, a.get_balance())

    def test_deposit_negative_money(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertFalse(a.deposit(-50))
        self.assertEqual(balance, a.get_balance())

    def test_deposit_zero_money(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertFalse(a.deposit(0))
        self.assertEqual(balance, a.get_balance())

    def test_deposit(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertTrue(a.deposit(500))
        self.assertEqual(balance + 500, a.get_balance())

    def test_withdraw_fail_negative_money(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertFalse(a.withdraw(-500))
        self.assertEqual(balance, a.get_balance())

    def test_withdraw_fail_zero_money(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertFalse(a.withdraw(0))
        self.assertEqual(balance, a.get_balance())

    def test_withdraw_fail_not_enough_money(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertFalse(a.withdraw(balance + 0.01))
        self.assertEqual(balance, a.get_balance())

    def test_withdraw_success_01(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertTrue(a.withdraw(balance))
        self.assertEqual(0, a.get_balance())

    def test_withdraw_success_02(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertTrue(a.withdraw(0.01))
        self.assertEqual(balance - 0.01, a.get_balance())

    def test_withdraw_success_03(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        a = Account(name, number, balance)
        self.assertTrue(a.withdraw(1234))
        self.assertEqual(balance - 1234, a.get_balance())

    def test_display_value(self):
        name = 'John Doe'
        number = 12345
        balance = 1500.00
        expected = '$1500.00'
        a = Account(name, number, balance)
        self.assertEqual(expected, str(a))

    def test_display_value2(self):
        name = 'John Doe'
        number = 12345
        balance = 1501.1
        expected = '$1501.10'
        a = Account(name, number, balance)
        self.assertEqual(expected, str(a))

    def test_display_value3(self):
        name = 'John Doe'
        number = 12345
        balance = .1
        expected = '$0.10'
        a = Account(name, number, balance)
        self.assertEqual(expected, str(a))

    def test_add_accounts(self):
        a = Account('John', 12345, 500)
        b = Account('Jaime', 54321, 10000)
        c = a + b
        d = b + c
        self.assertIsInstance(c, Account)
        self.assertEqual('John and Jaime', c.get_name())
        self.assertEqual(66666, c.get_number())
        self.assertEqual(10500, c.get_balance())
        e = a + b + c + d
        n = 'John and Jaime and John and Jaime and Jaime and John and Jaime'
        self.assertEqual(n, e.get_name())

if __name__ == '__main__':
    main()
