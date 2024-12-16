import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.lst = ['abc']
    def test_includes(self):
        self.assertNotIn('xyz',self.lst)
