'''
@author: Lilian
'''
import inspect
import unittest
from question_2 import molecule_to_list

class Question2Test(unittest.TestCase):


    def test_single_character(self):
        """
        Question 2: check that the function handles molecules composed of 
        single character molecules only.
        """
        self.assertEqual(molecule_to_list("H2O"), [('H',2), ('O',1)])
        self.assertEqual(molecule_to_list("CO2"), [('C',1), ('O',2)])
        self.assertEqual(molecule_to_list("C6H12O6"), [('C',6), ('H',12), ('O',6)])
        self.assertEqual(molecule_to_list("CH3COOH"), [('C',1), ('H',3), ('C',1), ('O',1), ('O',1), ('H',1)])
        
    def test_all(self):
        """
        Question 2: check that the function handles molecules composed of 
        single or multiple characters molecules.
        """
        self.assertEqual(molecule_to_list("CaCO3"), [('Ca',1), ('C',1), ('O',3)])
        self.assertEqual(molecule_to_list("NaHSO4"), [('Na',1), ('H',1), ('S',1), ('O',4)])
        self.assertEqual(molecule_to_list("Na2S2O7"), [('Na',2), ('S',2), ('O',7)])
        
    def test_error_alphasymbol(self):
        """
        Question 2: check that the function raises a ValueError if the molecule
        contains non alphabet symbols.
        """
        self.assertRaises(ValueError, molecule_to_list,"C++H3COOHCa")

    def test_error_firstsymbol(self):
        """
        Question 2: check that the function raises a ValueError if the molecule
        starts with a lower case character.
        """
        self.assertRaises(ValueError, molecule_to_list,"cO2")

    def test_error_symbol(self):
        """
        Question 2: check that the function raises a ValueError if the molecule
        contains an atom symbol starting with a lower case character.
        """
        self.assertRaises(ValueError, molecule_to_list,"H2o")



if __name__ == "__main__":
    unittest.main()
