import unittest

class NoExperienceError(AttributeError):
    pass

class Employee:
    def hire(self):
        raise NoExperienceError

class Test(unittest.TestCase):
    def setUp(self):
        self.employee = Employee()
    def test_includes(self):
        with self.assertRaises(NoExperienceError):
            self.employee.hire()
