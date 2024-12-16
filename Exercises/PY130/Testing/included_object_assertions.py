import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.lst = ['xyz']
    def test_includes(self):
        self.assertIn('xyz',self.lst)
