import unittest
from practical_5 import get_words_frequencies

class TestExo2(unittest.TestCase):

    def testEmptyText(self):
        self.assertEqual({}, get_words_frequencies(''))

    def testTextNoPunctuation(self):
        self.assertEqual({'to':2, 'be':2, 'or':1, 'not':1}, \
            get_words_frequencies('  to Be or Not TO be  '))

    def testTextWithPunctuation(self):
        self.assertEqual({'to':2, 'be':2, 'or':1, 'not':1}, \
            get_words_frequencies('. to Be, or Not TO be! '))

    def testTextWithNoDuplicate(self):
        self.assertEqual({'to':1, 'be':1, 'just':1,}, \
            get_words_frequencies('just to be'))

if __name__ == "__main__":
    unittest.main()
