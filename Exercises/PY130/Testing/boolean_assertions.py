import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.value = 3

    def test_is_odd(self):
        self.assertTrue(self.value % 2 != 0, 'Value is not odd')