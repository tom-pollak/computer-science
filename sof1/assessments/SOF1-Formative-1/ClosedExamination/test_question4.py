import unittest

from question_4 import scramble

class Question4Test(unittest.TestCase):
                              
    def test_scramble_6_chars(self):
        """Test if the function creates the two possible answers properly
        """
        for i in range(20):
            scrambled = scramble('python')
            self.assertTrue(scrambled in ['python', 'pyhton'],
                          "failed: scrambling 'python' should be equal to 'python' or 'pyhton'.")

    def test_scramble_5_chars(self):
        """Test if the function returns teh word itself if the size of the word is 5 or less
        """
        for i in range(20):
            self.assertTrue(scramble('snake') == 'snake',
                          "failed: scrambling 'snake' should be equal to 'snake' only.")

    def test_scramble_7_chars(self):
        """Test if the function creates all possible 7 letter variation of hearing.
        """
        for i in range(20):
            scrambled = scramble('hearing')
            self.assertTrue(scrambled in ['hearing', 'heairng', 'heiarng', 'heirang', 'heriang', 'heraing'],
                          "failed: scrambling 'hearing' should one of the following: 'hearing', 'heairng', 'heiarng', 'heirang', 'heriang', 'heraing'.")

    def test_scramble_7_properly(self):
        """Test if the function creates all possible 7 letter variation of hearing. 
        As the process is random, we must try many times (here 100) until all 
        possibilities are created.
        """
        possibilities = ['hearing', 'heairng', 'heiarng', 'heirang', 'heriang', 'heraing']
        outcomes = [0 for x in range(len(possibilities))]
        for i in range(100):
            outcomes[possibilities.index(scramble('hearing'))] += 1

        for x in outcomes:
            self.assertTrue(x>0,
                          "failed: scrambling 'hearing' should one of the following: 'hearing', 'heairng', 'heiarng', 'heirang', 'heriang', 'heraing'.")

