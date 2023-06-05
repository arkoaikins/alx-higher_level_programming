#!/usr/bin/python3
"""
a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
"""


class Rectangle:
    """
    class rectange with height and width attributes
    """
    def __init__(self, width=0, height=0):
        """
         Initializes the attributes of the rectange
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        to retrieve the width attribut
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting value for  width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        to retrieve the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates the area using the attributes and returns the
        area of the rectange
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates the perimter of the rectangle and return the
        perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        read = []
        for i in range(self.__height):
            [read.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                read.append("\n")
        return ("".join(read))
