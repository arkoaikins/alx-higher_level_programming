#!/usr/bin/python3
"""
 class Square that defines a square by: (based on 2-square.py)
"""


class Square():
    """ a class square"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """" current square area and returns the area"""
        return self.__size ** 2
