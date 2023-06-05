#!/usr/bin/python3
"""
Write a rectangle Class that defines a rectangle based on
0-rectangle.py
"""


class Rectangle:
    """
    class rectange with height and width attributes
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the attributes of the rectange
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """to retrieve the attribute height"""
        return self.__height

    @property
    def width(self):
        """ to retrieve the attribute width"""
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
