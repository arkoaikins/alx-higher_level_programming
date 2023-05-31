#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """ a class square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """calculates the square's area and returns it """
        return (self.__size) ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
