'''
@author: Lilian
'''
import inspect
import unittest
from question_5 import Blotris

class Question5iiTest(unittest.TestCase):


    def test_add(self):
        """
        Question 2.ii: check that the method can add a shape on the board.
        """
        game = Blotris(5,5)
        shape = [[1,1], 
                 [1,0], 
                 [1,0], 
                 [1,0]]
        self.assertTrue(game.add(shape, 0,0))
        list2D = [[1,1,0,0,0], 
                  [1,0,0,0,0], 
                  [1,0,0,0,0], 
                  [1,0,0,0,0], 
                  [0,0,0,0,0]]
        self.assertEqual(game._board,list2D)

        shape = [[0,1], 
                 [0,1], 
                 [0,1], 
                 [1,1]]
        self.assertTrue(game.add(shape, 1,0))
        list2D = [[1,1,0,0,0], 
                  [1,1,0,0,0], 
                  [1,1,0,0,0], 
                  [1,1,0,0,0], 
                  [1,1,0,0,0]]
        self.assertEqual(game._board,list2D)

       
        game = Blotris(8,5)
        shape = [[1,1], 
                 [1,0], 
                 [1,0], 
                 [1,0]]
        game._board = [[0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,1,1],
                       [0,0,0,0,1],
                       [1,0,1,1,1],
                       [1,0,0,1,1],
                       [1,0,1,1,1],
                       [1,1,0,1,0]]

        self.assertTrue(game.add(shape, 3,1))
        list2D = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,1,1],
                  [0,1,1,0,1],
                  [1,1,1,1,1],
                  [1,1,0,1,1],
                  [1,1,1,1,1],
                  [1,1,0,1,0]]
        self.assertEqual(game._board,list2D)


    def test_notadd_outofbounds(self):
        """
        Question 2.ii: check that the method does not add a shape if it is 
        out of bounds.
        """
        game = Blotris(5,5)
        shape = [[1,1], 
                  [1,0], 
                  [1,0], 
                  [1,0]]
        list2D = [[0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0]]
        self.assertFalse(game.add(shape, -1,0))
        self.assertEqual(game._board,list2D)

        self.assertFalse(game.add(shape, 1,-1))
        self.assertEqual(game._board,list2D)

        self.assertFalse(game.add(shape, 1,4))
        self.assertEqual(game._board,list2D)

        self.assertFalse(game.add(shape, 5,0))
        self.assertEqual(game._board,list2D)

    def test_notadd_overlaps(self):
        """
        Question 2.ii: check that the method does not add a shape if it 
        overlaps an existing object on the board.
        """
        game = Blotris(5,5)
        shape = [[1], 
                 [1], 
                 [1]]
        game._board = [[0,0,0,0,0], 
                       [0,0,0,0,0], 
                       [1,1,1,1,1], 
                       [0,0,0,0,0], 
                       [0,0,0,0,0]]
        self.assertFalse(game.add(shape, 1,2))
        list2D = [[0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [1,1,1,1,1], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0]]
        self.assertEqual(game._board,list2D)


        game = Blotris(8,5)
        shape = [[1,1], 
                  [1,0], 
                  [1,0], 
                  [1,0]]
        game._board = [[0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,1,1],
                       [0,0,0,0,1],
                       [1,0,1,1,1],
                       [1,0,0,1,1],
                       [1,0,1,1,1],
                       [1,1,0,1,0]]
        list2D = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,1,1],
                  [0,0,0,0,1],
                  [1,0,1,1,1],
                  [1,0,0,1,1],
                  [1,0,1,1,1],
                  [1,1,0,1,0]]

        self.assertFalse(game.add(shape, 3,0))
        self.assertEqual(game._board,list2D)

        



if __name__ == "__main__":
    unittest.main()
