#!/usr/bin/python3
"""
class rectange with height and width attributes
"""


class Rectangle:
    """Task 1: Is a Rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes the attributes of the rectange
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        To retrieve the attribute height
        """
        return self.__height

    @property
    def width(self):
        """
        To retrieve the attribute width
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
         setting value for  height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        setting value for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        returns the area of the reactangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__height + self.__width)
