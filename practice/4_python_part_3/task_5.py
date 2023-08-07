"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     # >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
from urllib import request

def make_request(url: str) -> Tuple[int, str]:
    try:
        response = request.urlopen(url)
        status_code = response.getcode()
        response_data = response.read().decode('utf-8')
        return status_code, response_data
    except Exception as e:
        return -1, str(e)

# Example usage
if __name__ == "__main__":
    url = 'https://www.google.com'
    status_code, response_data = make_request(url)
    print(status_code)
    print(response_data[:200])


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    'some text'
"""

import unittest
from unittest.mock import Mock, patch

class TestMakeRequest(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_make_request(self, mock_urlopen):
        # Simulate a successful response
        mock_response = Mock()
        mock_response.getcode.return_value = 200
        mock_response.read.return_value = b'response data'
        mock_urlopen.return_value = mock_response

        # Call the function with the mocked urlopen
        status_code, response_data = make_request('https://www.example.com')

        # Verify the output
        self.assertEqual(status_code, 200)
        self.assertEqual(response_data, 'response data')

if __name__ == '__main__':
    unittest.main()