import unittest
from unittest.mock import patch
from employee import Employee
# To enable: Shift+Ctrl+Alt+J
# To disable: SHIFT+ALT+INSERT


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Hasnine', 'Tushar', 5000)
        self.emp_2 = Employee('Tanvir', 'Azim', 7000)

    def tearDown(self):
        print('tearDown\n')
        
    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Hasnine.Tushar@email.com')
        self.assertEqual(self.emp_2.email, 'Tanvir.Azim@email.com')

        self.emp_1.first = 'Muhammad'
        self.emp_2.first = 'Muhammad'

        self.assertEqual(self.emp_1.email, 'Muhammad.Tushar@email.com')
        self.assertEqual(self.emp_2.email, 'Muhammad.Azim@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Hasnine Tushar')
        self.assertEqual(self.emp_2.fullname, 'Tanvir Azim')

        self.emp_1.first = 'Muhammad'
        self.emp_2.first = 'Muhammad'

        self.assertEqual(self.emp_1.fullname, 'Muhammad Tushar')
        self.assertEqual(self.emp_2.fullname, 'Muhammad Azim')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 7350)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Tushar/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Azim/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()

