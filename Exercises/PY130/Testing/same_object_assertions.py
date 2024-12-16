import unittest

class TestList:
    def process(self):
        return self

class Test(unittest.TestCase):
    def setUp(self):
        self.lst = TestList()
    def test_same_object(self):
        self.assertIs(self.lst, self.lst.process())

