'''
Created on 1 Dec 2016

@author: Lilian
'''
import inspect
import unittest
from question_2 import CarPark

class CarParkTest(unittest.TestCase):

    def test_park_vehicle(self):
        """
        Testing adding a series of vehicles in an empty car park. The last car 
        is to big to be parked in the car park.
        
        """
        carpark = CarPark(10)
        self.assertEqual(0, carpark.park_vehicle(2, 1), "Did not park the car at the expected position.")
        self.assertEqual([1,1,None,None,None,None,None,None,None,None], carpark._spaces, "Did not park the car at the expected position. The list _space is not modified correctly.")

        self.assertEqual(2, carpark.park_vehicle(3, 2), "Did not park the car at the expected position.")
        self.assertEqual([1,1,2,2,2,None,None,None,None,None], carpark._spaces, "Did not park the car at the expected position. The list _space is not modified correctly.")
        self.assertEqual(-1, carpark.park_vehicle(6, 3), "Parked a car when the car is too big for any available spot.")
        
    def test_park_vehicle_afterRemove(self):
        """
        Test several scenarios of parking cars when a slot has been freed by 
        another vehicle.
        - the car is too big for the freed slot, and should be park in the next 
          available slot
        - the car should park in the freed slot
        - the car is too big for all available slots.
        
        """
        carpark = CarPark(10)
        carpark._spaces = [1,1,None,None,None,3,None,None,None,None]
        self.assertEqual(6, carpark.park_vehicle(4, 4), "Did not park a car after the freed slot.")
        self.assertEqual([1,1,None,None,None,3,4,4,4,4], carpark._spaces, "Did not park the car at the expected position. The list _space is not modified correctly.")
        self.assertEqual(2, carpark.park_vehicle(2, 5), "Did not park a car in the freed slot.")
        self.assertEqual([1,1,5,5,None,3,4,4,4,4], carpark._spaces, "Did not park the car at the expected position. The list _space is not modified correctly.")
        self.assertEqual(-1, carpark.park_vehicle(2, 6), "Parked a car when the car is too big for any available spot.")

        
    def test_park_vehicle_Error(self):
        """
        Test the park_vehicle method. In this test we check the following
        requirements:
        - we cannot park an already parked car (same uid) in the car park
        
        """
        carpark = CarPark(10)
        carpark._spaces = [1,1,None,None,None,3,None,None,None,None]
        
        # check cannot park an already parked car (same uid) in the car park
        self.assertRaises(ValueError, carpark.park_vehicle, 1, 3)
             


if __name__ == "__main__":
    unittest.main()
