import unittest

class Numeric:
    pass

class Test(unittest.TestCase):
    def setUp(self):
        self.value = Numeric()

    def test_type(self):
        self.assertIsInstance(self.value, Numeric)