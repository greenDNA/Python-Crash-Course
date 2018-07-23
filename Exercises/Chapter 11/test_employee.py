import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('Kate', 'Madison', 74000)

    def test_give_default_raise(self):
        record = self.my_employee.annual_salary
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, record+5000)

    def test_give_custom_raise(self):
        record = self.my_employee.annual_salary
        custom = 12345
        self.my_employee.give_raise(custom)
        self.assertEqual(self.my_employee.annual_salary, record + custom)

unittest.main()
