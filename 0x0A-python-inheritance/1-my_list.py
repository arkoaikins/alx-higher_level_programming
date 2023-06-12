#!/usr/bin/python3
"""
 class MyList that inherits from list
"""


class MyList(list):
    """ set a MyList class"""
    def print_sorted(self):
        """
        print_sorte -  prints the list, but sorted (ascending sort)
        """
        if not all(isinstance(i, int) for i in self):
            "raise type error all instances are not type int"""
            raise TypeError("must be a list of integers")
        print(sorted(self))
