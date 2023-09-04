#!/usr/bin/python3
"""Module contains dummy addition function for testing"""


def add_integer(a, b=98):
    """ adds integers
        Arguments:
        @a: first integer
        @b: second integer, defaults to 98 if not specified
    """

    If type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    If type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    Return int(a) + int(b)
