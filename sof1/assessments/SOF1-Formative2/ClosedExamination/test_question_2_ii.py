'''
Created on 1 Dec 2016

@author: Lilian
'''
import inspect
import unittest
from question_2 import CarPark

class CarParkTest(unittest.TestCase):

    def test_get_available_space(self):
        """
        Test if the constructor builds an instance (2 marks). Then test if 
        get_available_space works on an empty car park (4 marks).
        
        """
        carpark = CarPark(10)
        self.assertEqual(10, carpark.get_available_spaces(0), 
                          "Cannot return the number of available spaces in an empty car park.")

        # Ensure that count starts form position and previous empty
        # spots are not counted.
        self.assertEqual(5, carpark.get_available_spaces(5), 
                          "Cannot return the right number of available spaces in the middle of an empty spot.")
        
    def test_get_available_space_withaddedCar(self):
        """
        Test get_available_space once cars have been added and removed
        
        """
        carpark = CarPark(10)
        carpark._spaces = [1,1,None,None,None,None,None,None,None,None]
        
        # Ensure that the method returns 0 if a car is parked at that 
        # position
        self.assertEqual(0, carpark.get_available_spaces(1), 
                          "Did not return 0 available space when the slot is already occupied.")
        
        carpark._spaces = [1,1,None,None,None,3,3,None,None,None]
        self.assertEqual(3, carpark.get_available_spaces(2), 
                          "Did not return the right number of available space once a car has been removed.")
        
        # Ensure that count starts form position and previous empty
        # spots are not counted.
        self.assertEqual(2, carpark.get_available_spaces(3), 
                          "Did not return the right number of available space once a car has been removed.")



if __name__ == "__main__":
    unittest.main()
