import unittest

from question_3 import sum_integers


class Question3Test(unittest.TestCase):
                              
    def testSumNormal(self):
        """Test if the sum is correct when correct positive inputs are given
        """
        self.assertEqual(10, sum_integers(0,4),
                          "failed: Sum of positive number is incorrect")
         
    def testSumNormalEquals(self):
        """Test if the sum is correct when the two inputs are equal
        """       
        self.assertEqual(5, sum_integers(5, 5), 
                          "failed: When the two inputs are equal, should return the input value.")
         
    def testSumValueError1(self):
        """Test if a  -1  is returned when
           the second input is smaller than the first
        """       
        self.assertEqual(-1, sum_integers(5, 4), 
                          "failed: should return -1.")
        
    def testSumValueError2(self):
        """Test if a -1 is returned when at least one of the parameters is negative
        """       
        self.assertEqual(-1, sum_integers(-5, 4), 
                          "failed: should return -1.")       
        self.assertEqual(-1, sum_integers(5, -4), 
                          "failed: should return -1.")
        

