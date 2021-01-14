'''
@author: Lilian
'''
import inspect
import unittest
from question_3 import ATOMS, molar_mass

class Question3Test(unittest.TestCase):


    def test_molecules(self):
        """
        Question 3: check that the function computes the correct molecular mass
        of a valid molecule.
        """
        self.assertAlmostEqual(molar_mass([('H',2), ('O',1)]), 18.01534, 5)
        self.assertAlmostEqual(molar_mass([('C',1), ('O',2)]), 44.0098, 5)
        self.assertAlmostEqual(molar_mass([('C',1), ('H',3), ('C',1), ('O',1), ('O',1), ('H',1)]), 60.052679, 5)
        
        
    def test_error_molecule(self):
        """
        Question 3: check that the function raises a ValueError if the molecule
        contains an unknown atom (symbol).
        """
        self.assertRaises(ValueError, molar_mass,[('Cb',2), ('S',2), ('O',7)])




if __name__ == "__main__":
    unittest.main()
