# Testing a name_function.py

from name_function import get_formatted_name
import unittest

class NameTestCase(unittest.TestCase):
    """Test to check the functioning of name_function.py"""

    def test_first_last_name(self):
        """Do names like Debopriyo Bhowmick work ?"""
        formatted_name = get_formatted_name('debopriyo', 'bhowmick')
        self.assertEqual(formatted_name, 'Debopriyo Bhowmick')

if __name__ == '__main__':
    unittest.main()
