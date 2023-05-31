#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """ a class square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """calculates the square's area and returns it"""
        return (self.__size) ** 2

    @property
    def size(self):
        """Returns size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """Prints the square with # to stdout"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
