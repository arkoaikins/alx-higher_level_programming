#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 4-square.py)
"""


class Square():
    """a class square"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.__size = size

    @property
    def size(self):
        """Returns size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size"""
        if isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculate the square
        and returns the area of a Square object
        """
        return self.__size ** 2

    def __eq__(self, other) -> bool:
        """ object areas are equal-checks"""
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        """areas are not equal - checks"""
        return self.area() != other.area()

    def __gt__(self, other) -> bool:
        """one object area is greater than another- checks"""
        return self.area() > other.area()

    def __ge__(self, other) -> bool:
        """one object area is greater than or equal to another -checks"""
        return self.area() >= other.area()

    def __lt__(self, other) -> bool:
        """one object area is less than another- checks"""
        return self.area() < other.area()

    def __le__(self, other) -> bool:
        """one object area is less than or equal to another- checks"""
        return self.area() <= other.area()
