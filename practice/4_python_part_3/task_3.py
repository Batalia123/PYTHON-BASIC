"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    # >>> is_http_domain('http://wikipedia.org')
    True
    # >>> is_http_domain('https://ru.wikipedia.org/')
    True
    # >>> is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain: str) -> bool:
    pattern = r'^https?://?([\w-]+\.)+[\w]+(/[\w-]+)*/?$'
    return bool(re.match(pattern, domain))


"""
write tests for is_http_domain function
"""
import unittest

class TestIsHttpDomain(unittest.TestCase):

    def test_valid_domains(self):
        valid_domains = [
            ('http://wikipedia.org', True),
            ('https://ru.wikipedia.org/', True),
            ('https://example.com/somepath', True),
        ]
        for domain, expected_result in valid_domains:
            with self.subTest(domain=domain):
                self.assertEqual(is_http_domain(domain), expected_result)

    def test_invalid_domains(self):
        invalid_domains = [
            ('griddynamics.com', False),
            ('http://invalid..domain/', False),
            ('ftp://example.com', False),
            ('https://invalid_domain', False),
        ]
        for domain, expected_result in invalid_domains:
            with self.subTest(domain=domain):
                self.assertEqual(is_http_domain(domain), expected_result)


if __name__ == "__main__":
    unittest.main()
