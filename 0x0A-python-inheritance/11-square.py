#!/usr/bin/python3
"""
a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)
"""


Rectangle = __import__('9-rectangle').Rectangle
"""import the 9-rectangle module to be able to use it """


class Square(Rectangle):
    """
    A class square inheriting Rectangle.
    """
    def __init__(self, size):
        """
        Initialization of the square with size attribute
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = 
