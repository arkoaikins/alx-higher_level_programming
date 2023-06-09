#!/usr/bin/python3
"""
 a function that prints a square with the character #.
"""


def print_square(size):
    """
    print_square - prints a square with the character #

    args: size =  the size length of the square
    return: prints the #

    """
    if type(size) is not int:
        """
        raises type error if size is not an integer
        """
        raise TypeError("size must be an integer")
    if size < 0:
        """
         raises type error if size is not greater or equal to 0
        """
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
