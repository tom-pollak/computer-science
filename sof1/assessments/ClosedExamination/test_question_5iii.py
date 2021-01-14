'''
@author: Lilian
'''
import inspect
import unittest
from question_5 import Blotris

class Question5iiiTest(unittest.TestCase):


    def test_update_singleline(self):
        """
        Question 2.iii: Check if update can remove a single full row.
        """
        game = Blotris(5,5)
        game._board = [[0,0,0,0,0], 
                       [0,0,0,0,0], 
                       [1,0,1,0,0], 
                       [1,0,1,1,0], 
                       [1,1,1,1,1]]
        list2D = [[0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [1,0,1,0,0], 
                  [1,0,1,1,0]]
        game.update()
        self.assertEqual(game._board,list2D)

        game._board = [[1,1,0,0,0], 
                       [1,1,1,1,1], 
                       [1,0,0,0,0], 
                       [1,0,0,0,0], 
                       [0,0,0,0,0]]
        list2D = [[0,0,0,0,0], 
                  [1,1,0,0,0], 
                  [1,0,0,0,0], 
                  [1,0,0,0,0], 
                  [0,0,0,0,0]]
        game.update()
        self.assertEqual(game._board,list2D)


       
    def test_update_multiline(self):
        """        
        Question 2.iii: Check if update can remove multiple full rows.
        """
        game = Blotris(8,5)
        game._board = [[0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,1,1],
                       [0,1,1,0,1],
                       [1,1,1,1,1],
                       [1,1,0,1,1],
                       [1,1,1,1,1],
                       [1,1,0,1,0]]

        list2D = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,1,1],
                  [0,1,1,0,1],
                  [1,1,0,1,1],
                  [1,1,0,1,0]]
        game.update()
        self.assertEqual(game._board,list2D)


    def test_removeall(self):
        """
        Question 2.iii: Check if update empty all rows of an entirely full 
        board.
        """
        game = Blotris(5,5)
        shape = [[1,1], 
                  [1,0], 
                  [1,0], 
                  [1,0]]
        game._board = [[1,1,1,1,1], 
                       [1,1,1,1,1], 
                       [1,1,1,1,1], 
                       [1,1,1,1,1], 
                       [1,1,1,1,1]]

        list2D = [[0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0], 
                  [0,0,0,0,0]]
        game.update()
        self.assertEqual(game._board,list2D)

    def test_nochange(self):
        """
        Question 2.iii: Check if update does not modify a boar if no row are 
        full.
        """
        game = Blotris(5,5)
        shape = [[1,1], 
                  [1,0], 
                  [1,0], 
                  [1,0]]
        game._board = [[1,1,0,1,1], 
                       [1,0,1,1,1], 
                       [1,1,1,0,1], 
                       [1,1,1,1,0], 
                       [1,0,1,1,1]]

        list2D = [[1,1,0,1,1], 
                  [1,0,1,1,1], 
                  [1,1,1,0,1], 
                  [1,1,1,1,0], 
                  [1,0,1,1,1]]

        game.update()
        self.assertEqual(game._board,list2D)




if __name__ == "__main__":
    unittest.main()
