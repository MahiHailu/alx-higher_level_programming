#!/usr/bin/python3

"""Define the inherited list class MyList."""


class MyList(list):
    """implements sorted printing for built-in list classes."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
