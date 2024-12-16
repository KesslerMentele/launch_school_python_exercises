import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.value = 'XYZ'
    def test_lower(self):
        self.assertEqual('xyz', self.value.lower())
