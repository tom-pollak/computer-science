import unittest

from question_1 import create_triangle

class Question1Test(unittest.TestCase):
                              
    def test_create_size4(self):
        """Test if triangle of even rows are created properly
        """
        self.assertEqual('x---\nxx--\nxxx-\nxxxx\n', create_triangle(4),
                          "failed: cannot create a triangle of size 4. Check for missing \\n.")

    def test_create_size5(self):
        """Test if triangle of odd rows are created properly
        """
        self.assertEqual('x----\nxx---\nxxx--\nxxxx-\nxxxxx\n', 
                         create_triangle(5),
                         "failed: cannot create a triangle of size 5. Check for missing \\n.")

    def test_create_size0(self):
        """Test if triangle of size 0 is an empty string
        """
        self.assertEqual('', 
                         create_triangle(0),
                         "failed: cannot create a triangle of size 0. Should be an empty string.")

    def test_create_invalidsize(self):
        """Test if creating a triangle of negative size returns None
        """
        self.assertIsNone(create_triangle(-1),
                         "failed: cannot create a triangle of negative size. Should return None.")

