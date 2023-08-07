"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    #>>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    662
    #>>> calculate_days('2021-10-05')
    664
    #>>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime
import re
from freezegun import freeze_time
import pytest

class WrongFormatException(Exception):
    "Raised when the date format doesn't match"
    pass


def calculate_days(from_date: str) -> int:
    pattern = '^\d{4}-\d{2}-\d{2}$'
    try:
        if not re.match(pattern, from_date):
            raise WrongFormatException('Wrong date format provided')
        from_datetime_object = datetime.strptime(from_date, '%Y-%m-%d')
        now_datetime_object = datetime.now()
        return (now_datetime_object - from_datetime_object).days
    except WrongFormatException:
        print('WrongFormatException')



"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""

# Tests for calculate_days function
def test_calculate_days_past_date():
    # Mock the current date to October 6, 2021
    with freeze_time("2021-10-06"):
        assert calculate_days('2021-10-07') == -1
        assert calculate_days('2021-10-05') == 1

def test_calculate_days_future_date():
    # Mock the current date to October 6, 2021
    with freeze_time("2021-10-06"):
        assert calculate_days('2021-10-08') == -2


def test_calculate_days_today():
    # Mock the current date to October 6, 2021
    with freeze_time("2021-10-06"):
        assert calculate_days('2021-10-06') == 0

def test_calculate_days_leap_year():
    # Mock the current date to February 28, 2024 (leap year)
    with freeze_time("2024-02-28"):
        assert calculate_days('2024-02-29') == -1

def test_calculate_days_leap_year_future_date():
    # Mock the current date to February 28, 2024 (leap year)
    with freeze_time("2024-02-28"):
        assert calculate_days('2024-03-01') == -2

if __name__ == "__main__":
    test_calculate_days_past_date()
    test_calculate_days_future_date()
    test_calculate_days_today()
    test_calculate_days_leap_year()
    test_calculate_days_leap_year_future_date()