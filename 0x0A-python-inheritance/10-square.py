#!/usr/bin/python3
"""
a class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle
""" import the 9-rectange to use it"""


class Square(Rectangle):
    """A class square inheriting a rectangle"""
    def __init__(self, size):
        """instantiation of the square with sieze"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"return the area of the square"""
        return self.__size ** 2
