#!/usr/bin/python3
"""
 Module of class disallowing creation of dynamic attributes

"""


class LockedClass():
    """Class to prevent creation of dynamic attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
