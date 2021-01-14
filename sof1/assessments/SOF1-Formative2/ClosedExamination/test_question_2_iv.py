'''
Created on 1 Dec 2016

@author: Lilian
'''
import inspect
import unittest
from question_2 import CarPark

class CarParkTest(unittest.TestCase):
    
    def test_remove_vehicle(self):
        """
        Test the remove_vehicle method. In this test we check the following
        requirements:
        - we cannot remove a car from an empty car park
        - we can remove an existing car
        - a car cannot be removed a second time
        - the space has been freed properly
        
        """
        carpark = CarPark(10)
        
        # Check that we cannot remove a car from an empty car park
        self.assertFalse(carpark.remove_vehicle(2), 
                         "Should not be able to remove successfully a car that is not in the car park.")

        carpark._spaces = [1,1,2,2,2,3,None,None,None,None]        
        # Remove an existing car
        self.assertTrue(carpark.remove_vehicle(2), "Did not remove successfully a car, failed to return True")
        self.assertEqual([1,1,None,None,None,3,None,None,None,None], carpark._spaces, "Did not remove successfully a car, failed to remove the car id from the list _space")
        
        # Check a car cannot be removed a second time
        self.assertFalse(carpark.remove_vehicle(2), "Has 'removed' a car that has already been removed.")

        self.assertTrue(carpark.remove_vehicle(3), "Did not remove successfully a car, failed to return True")
        self.assertTrue(carpark.remove_vehicle(1), "Did not remove successfully a car, failed to return True")
     
        self.assertEqual([None,None,None,None,None,None,None,None,None,None], carpark._spaces)
         


if __name__ == "__main__":
    unittest.main()
