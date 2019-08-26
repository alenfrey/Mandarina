"""
This module contains functions to generate random data
"""

import random
import string
import datetime


def random_string(length=6, chars=string.ascii_letters):
    """
    This function generates random strings with specified lengths.
    :param length: Length of the random string
    :param chars: Charset to choose chracters from
    :return: Randomly generated string
    """
    return "".join(random.choice(chars) for _ in range(length))


def random_datetime(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    :param start: Startdate
    :param end: Enddate
    :return: A random Datetime object
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)
