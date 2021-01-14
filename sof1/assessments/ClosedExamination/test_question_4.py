'''
@author: Lilian
'''
import inspect
import unittest
from question_4 import check_level

class Question4Test(unittest.TestCase):


    def test_feasible(self):
        """
        Question 4: check that the function returns True if a level is feasible.
        """
        self.assertTrue(check_level([1,1,1,1,1]))
        self.assertTrue(check_level([1,2,0,1,2]))
        self.assertTrue(check_level([3,1,2,0,4,0,1]))
        self.assertTrue(check_level([4,0,0,0,1]))
       
    def test_unfeasible(self):
        """
        Question 4: check that the function returns False if a level is 
        unfeasible. That is, starts or ends with a mine (0), or lands on a 
        mine whatever the move taken.
        """
        self.assertFalse(check_level([0,1,1,1,1]))
        self.assertFalse(check_level([2,0,3,0]))
        self.assertFalse(check_level([3,2,1,0,2,0,2]))
        self.assertFalse(check_level([2,3,0,2,1,0,2]))
        



if __name__ == "__main__":
    unittest.main()
