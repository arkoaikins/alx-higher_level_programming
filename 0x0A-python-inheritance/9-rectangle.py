#!/usr/bin/python3
"""
a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
importing the 7-base_geometry as a module
"""


class Rectangle(BaseGeometry):
    """
    A Class Rectangle  BaseGeometry
    """
    def __init__(self, width, height):
        """
        initialization with width and height attributes
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        implementation of the area method
        """
        return self.__height * self.__width

    def __str__(self):
        """
        str return the [Rectangle] <width>/<height> rectangle
        description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
