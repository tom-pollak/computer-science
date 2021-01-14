'''
Created on 1 Dec 2016

@author: Lilian
'''
import inspect
import unittest
from question_2 import CarPark

class CarParkTest(unittest.TestCase):


    def test_constructor(self):
        """
        Test if the constructor create a list of the given size.
        
        """
        carpark = CarPark(2)
        self.assertEqual([None, None], carpark._spaces)
        
    def test_constructor_error(self):
        """
        Test if the constructor raises a ValueError when an invalid size is
        given.
        
        """
        self.assertRaises(ValueError, CarPark, 0)
        self.assertRaises(ValueError, CarPark, -2)
        


if __name__ == "__main__":
    unittest.main()
