'''
@author: Lilian
'''
import inspect
import unittest
from question_5 import Blotris

class Question5iTest(unittest.TestCase):


    def test_init(self):
        """
        Question 2.i: check that the method creates an empty the board.
        """
        game = Blotris(5,5)
        list2D = [[0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0]]
        self.assertEqual(game._board, list2D)
       
        game = Blotris(5,6)
        list2D = [[0,0,0,0,0,0], 
                  [0,0,0,0,0,0], 
                  [0,0,0,0,0,0], 
                  [0,0,0,0,0,0], 
                  [0,0,0,0,0,0]]
        self.assertEqual(game._board, list2D)


    def test_error_size(self):
        """
        Question 2.i: check that the method raises a ValueError if the size 
        parameters are invalid (less than 5).
        """
        self.assertRaises(ValueError, Blotris, 4,5)
        self.assertRaises(ValueError, Blotris, 5,4)
        self.assertRaises(ValueError, Blotris, -5,-4)
        



if __name__ == "__main__":
    unittest.main()
