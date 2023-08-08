"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     # >>> make_request('https://www.google.com')
     200, 'response data'
"""
import urllib.request
import ssl


def make_request(url):
    try:
        # Create an SSL context that doesn't verify certificates
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        response = urllib.request.urlopen(url, context=ssl_context)
        status_code = response.getcode()
        response_data = response.read().decode('utf-8')
        return status_code, response_data
    except urllib.error.URLError as e:
        print(f"Error making request: {e}")
        return None, None


# Example usage
if __name__ == '__main__':
    url = 'https://www.google.com'
    status_code, response_data = make_request(url)
    if status_code is not None and response_data is not None:
        print(status_code)
        print(response_data)
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
    def test_make_request_success(self, mock_urlopen):
        mock_response = Mock()
        mock_response.getcode.return_value = 200
        mock_response.read.return_value = b'response data'
        mock_urlopen.return_value = mock_response

        url = 'https://www.example.com'
        status_code, response_data = make_request(url)

        self.assertEqual(status_code, 200)
        self.assertEqual(response_data, 'response data')

    @patch('urllib.request.urlopen')
    def test_make_request_error(self, mock_urlopen):
        # Set up the mock to raise an URLError
        mock_urlopen.side_effect = urllib.error.URLError('Mocked error')

        url = 'https://www.example.com'
        status_code, response_data = make_request(url)

        self.assertIsNone(status_code)
        self.assertIsNone(response_data)


if __name__ == '__main__':
    unittest.main()
