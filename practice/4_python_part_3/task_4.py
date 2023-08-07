"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse


import argparse
from faker import Faker
import json

def generate_dicts(number, fields):
    fake = Faker()
    dicts = []
    for _ in range(number):
        data = {}
        for field in fields:
            key, provider = field.split('=')
            data[key] = getattr(fake, provider)()
        dicts.append(data)
    return dicts

def print_name_address(args: argparse.Namespace) -> None:
    number = int(args.number)
    fields = args.fields
    dicts = generate_dicts(number, fields)
    for data in dicts:
        print(json.dumps(data))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate dicts with fake data.")
    parser.add_argument("number", help="Number of generated instances", type=int)
    parser.add_argument("--fields", nargs='+', help="Key and provider pairs", required=True)
    args = parser.parse_args()
    print_name_address(args)

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""


import unittest
from unittest.mock import Mock, patch

class TestPrintNameAddress(unittest.TestCase):

    @patch('builtins.print')
    def test_print_name_address(self, mock_print):
        mock_args = Mock()
        mock_args.number = 2
        mock_args.fields = ['fake-address=address', 'some_name=name']

        print_name_address(mock_args)

        actual_calls = mock_print.call_args_list

        for actual_call in actual_calls:
            call_args, _ = actual_call
            generated_dict_str = call_args[0]
            generated_dict = eval(generated_dict_str)
            self.assertTrue("some_name" in generated_dict)
            self.assertTrue("fake-address" in generated_dict)

if __name__ == '__main__':
    unittest.main()