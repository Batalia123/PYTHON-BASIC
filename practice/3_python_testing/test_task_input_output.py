"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
import unittest
from unittest.mock import patch
import sys
sys.path.append('/Users/nwykpis/PYTHON-BASIC/practice/2_python_part_2')

from task_input_output import *


class TestReadNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', 'hello', '2', 'world'])
    def test_read_numbers_with_mixed_input(self, mock_input):
        result = read_numbers(5)
        self.assertEqual(result, "Avg: 1.67")

    @patch('builtins.input', side_effect=['hello', 'world', 'foo', 'bar', 'baz'])
    def test_read_numbers_with_no_numbers(self, mock_input):
        result = read_numbers(5)
        self.assertEqual(result, "No Numbers entered")

if __name__ == '__main__':
    unittest.main()
