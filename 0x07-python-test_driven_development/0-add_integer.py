#!/usr/bin/python3
"""
 A function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    add_integer - adds 2 integers
    args: a = first int
          b = second int
          float will be caseted to int
    Return: integer
    """
    if not isinstance(a, (int, float)):
        """
        raises type error when a is  not an int
        """
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        """
        raises type error when b is not an int
        """
        raise TypeError("b must be an integer")

    result = a + b
    if result == float('inf') or result == float('-inf'):
        raise OverflowError("float overflow")
    return int(a) + int(b)
