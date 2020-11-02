import unittest
from practical_5 import rasterise

class TestExo4(unittest.TestCase):

    def testInvalidWidth(self):
        self.assertEqual(None, rasterise([1,2,3], 0))

    def testNegativeWidth(self):
        self.assertEqual(None, rasterise([1,2,3], -1))

    def testNotMultipleWidth(self):
        self.assertEqual(None, rasterise([1,2,3], 2))

    def testSameWidth(self):
        self.assertEqual([[1,2,3]], rasterise([1,2,3], 3))

    def testWidthOne(self):
        self.assertEqual([[1],[2],[3]], rasterise([1,2,3], 1))

    def testMultipleWidth(self):
        self.assertEqual([[1,2],[3,4],[5,6],[7,8]], rasterise([1,2,3,4,5,6,7,8], 2))
        self.assertEqual([[1,2,3,4],[5,6,7,8]], rasterise([1,2,3,4,5,6,7,8], 4))

if __name__ == "__main__":
    unittest.main()
