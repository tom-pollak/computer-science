import unittest
from practical_5 import split_text

class TestExo1(unittest.TestCase):

    def testEmptyText(self):
        self.assertEqual([], split_text(""))

    def testTextOnlyWhiteSpace(self):
        self.assertEqual(["As", "Python's", "creator,", "I'd", "like", "to", "say"], \
            split_text("As Python's creator, I'd like to say ",' '))

    def testTextWithMultipleDelimiters(self):
        self.assertEqual(["As", "Python", "s", "creator", "I", "d", "like", "to", "say"], \
            split_text("  As Python's creator, I'd like to say  ",", '"))

    def testTextWithSingleDelimiter(self):
        self.assertEqual(["  As Python's creator", " I'd like to say  "], \
            split_text("  As Python's creator, I'd like to say  ", ','))

    def testTextWithoutRightDelimiter(self):
        self.assertEqual(["  As Python's creator, I'd like to say  "], \
            split_text("  As Python's creator, I'd like to say  ", "!>"))

if __name__ == "__main__":
    unittest.main()
