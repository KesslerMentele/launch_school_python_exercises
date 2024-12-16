import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.value = None
    def test_none(self):
        self.assertIsNone(self.value)
