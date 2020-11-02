import unittest
import inspect
from sumevens import sum_even_numbers

class TestSumEvens(unittest.TestCase):
    
    def testEmptyList(self):
        self.assertEqual(0, sum_even_numbers([]))
         
    def testEvensOnly(self):
        self.assertEqual(12, sum_even_numbers([2,4,6]))

    def testOddsOnly(self):
        self.assertEqual(0, sum_even_numbers([1,3,5,7]),\
            "the sum should be 0 is list contains only odd numbers")
         
    def testSumEvens(self):
        self.assertEqual(10, sum_even_numbers([1,2,3,4]))
         

if __name__ == "__main__":
    unittest.main()
