
import unittest

from question_2 import create_chequerboard


class Question2Test(unittest.TestCase):
                              
    def test_create_size4(self):
        """Test if boards of even rows are created properly
        """
        self.assertEqual('x-x-\n-x-x\nx-x-\n-x-x\n', create_chequerboard(4),
                          "failed: cannot create a board of size 4. Check for missing \\n.")

    def test_create_size5(self):
        """Test if boards of odd rows are created properly
        """
        self.assertEqual('x-x-x\n-x-x-\nx-x-x\n-x-x-\nx-x-x\n', create_chequerboard(5),
                          "failed: cannot create a board of size 5. Check for missing \\n.")

    def test_create_size2(self):
        """Test if boards of 2 rows are created properly
        """
        self.assertEqual('x-\n-x\n', create_chequerboard(2),
                          "failed: cannot create a board of size 2. Check for missing \\n.")

    def test_create_invalidsize(self):
        """Test if boards of invalide size returns None
        """
        self.assertIsNone(create_chequerboard(1),
                          "failed: a board of size < 2 should return None.")


