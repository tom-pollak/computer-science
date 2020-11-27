import unittest
from practical_5 import flatten

class TestExo3(unittest.TestCase):

    def testFlatten(self):
        self.assertEqual([1,2,3,7,8], flatten([[1,2],[3,7],[8]]))

    def testEmptyList(self):
        self.assertEqual([1,2,7], flatten([[1,2],[],[7],[]]))

    def testDuplicate(self):
        self.assertEqual([1,2,2,3,7,8,7], flatten([[1,2],[2,3],[7],[8,7]]))

    def testSingleElement(self):
        self.assertEqual([1,2,2,3,7,8,7], flatten([[1,2,2,3,7,8,7]]))

if __name__ == "__main__":
    unittest.main()
