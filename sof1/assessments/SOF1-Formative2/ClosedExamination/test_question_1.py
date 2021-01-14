'''
Created on 1 Dec 2016

@author: Lilian
'''
import unittest
import inspect
from question_1 import text2dictionary


class Question1Test(unittest.TestCase):
    

    def test_text2dictionary(self):
        """
        text2dictionary:
        Test if function can deal with multiple airports in same country
        """
        
        dico = text2dictionary("data/airport_data.txt")
        self.assertCountEqual([('Aberdeen', 'ABR')], dico['USA'])
        self.assertCountEqual([('Agen', 'AGF'), ('Ajaccio', 'AJA')], dico['France'])

    def test_text2dictionary_duplicates(self):
        """
        text2dictionary:
        Test if function removes duplicates
        """
        dico = text2dictionary("data/airport_data_duplicates.txt")
        self.assertCountEqual([('Agen', 'AGF'), ('Ajaccio', 'AJA')], dico['France'])
        
    def test_text2dictionary_completeness(self):      
        """
        text2dictionary:
        Test if function works correctly with the given text file
        """
        data = {'India': [('Agra', 'AGR'), ('Ahmedabad', 'AMD'), ('Aizawl', 'AJL')], 
                'Marshall Islands': [('Ailuk Island', 'AIM'), ('Airok', 'AIC')], 
                'United Kingdom': [('Aberdeen', 'ABZ')], 
                'China': [('Aksu', 'AKU')], 
                'Mexico': [('Aguascalientes', 'AGU')], 
                'Turkey': [('Agri', 'AJI')], 
                'Papua New Guinea': [('Agaun', 'AUP')], 
                'France': [('Agen', 'AGF'), ('Ajaccio', 'AJA')], 
                'Cook Islands': [('Aitutaki', 'AIT')], 
                'Japan': [('Aguni', 'AGJ'), ('Akita', 'AXT')], 
                'Puerto Rico': [('Aguadilla', 'BQN')], 
                'Mauritania': [('Aioun El Atrouss', 'AEO')], 
                'USA': [('Aberdeen', 'ABR')], 
                'Iran': [('Ahwaz', 'AWZ')]}

        dico = text2dictionary("data/airport_data.txt")  
        for entry in data:
            self.assertCountEqual(data[entry], dico[entry])

    def test_text2dictionary_Error_toomanyentries(self):
        """
        text2dictionary:
        Test if function raises an IOError when there are too many entries
        per line
        """
        self.assertRaises(IOError, text2dictionary, "data/airport_data_invalid_extraEntry.txt")
        
    def test_text2dictionary_Error_missingentries(self):
        """
        text2dictionary:
        Test if function raises an IOError when there are too few entries
        per line
        """
        self.assertRaises(IOError, text2dictionary, "data/airport_data_invalid_missingEntry.txt")
        
    def test_text2dictionary_Error_codeTooLong(self):
        """
        text2dictionary:
        Test if function raises an IOError when the airport code is too long
        """
        self.assertRaises(IOError, text2dictionary, "data/airport_data_invalid_longcode.txt")
        
    def test_text2dictionary_Error_codeTooShort(self):
        """
        text2dictionary:
        Test if function raises an IOError when the airport code is too short
        """
        self.assertRaises(IOError, text2dictionary, "data/airport_data_invalid_shortcode.txt")
        


if __name__ == "__main__":
    unittest.main()
