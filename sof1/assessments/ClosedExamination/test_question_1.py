'''
@author: Lilian
'''
import unittest
import inspect
from question_1 import encrypt


class Question1Test(unittest.TestCase):
    

    def test_encrypt(self):
        """
        Question 1: check that the function encrypt a valid message. Check it 
        works with different alphabet.
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.assertEqual(encrypt('BABY', [1,1,1,1], alphabet), 'CBCZ')
        self.assertEqual(encrypt('BABY', [2,1,1,3], alphabet), 'DBCB')
        self.assertEqual(encrypt('BAC', [2,1,3], 'ABCDE'), 'DBA')


    def test_error_shift_length(self):
        """
        Question 1: check that the function raises a ValueError if the size of
        the list of shifts is invalid.
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.assertRaises(ValueError, encrypt, 'BABY', [2,1,1], alphabet)
        self.assertRaises(ValueError, encrypt, 'BABY', [2,1,1,2,3], alphabet)
        
    def test_error_shift_negative_value(self):
        """
        Question 1: check that the function raises a ValueError if one of the
        shifts is invalid (negative).
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.assertRaises(ValueError, encrypt, 'BABY', [2,1,1,-1], alphabet)
        
    def test_error_shift_value_toobig(self):
        """
        Question 1: check that the function raises a ValueError if one of the
        shifts is invalid (greater than the length of the alphabet).
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.assertRaises(ValueError, encrypt, 'BABY', [2,1,1,27], alphabet)
        


if __name__ == "__main__":
    unittest.main()
