#!/usr/bin/python3
"""
A class rectangle that inherits from the base
"""


from models.base import Base


class Rectangle(Base):
    """
    A class rectangle
    which inherits from the base

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization with widht,height, x,y and id attributes
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        """
        set each prive attribute with it's own public
        getter and setter

        task 2 ends here
        """

    @property
    def width(self):
        """
        task 2:
        assigning the width argument to the right attribute
        """
        return self.__width

        """
        Task 3
        Updating the Class Reactangle by adding all setter instantiation
        """
    @width.setter
    def width(self, value):
        """
        adding the width setter with exceptions
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        task 2:
        assigning the height argument to the right attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        adding the height setter with exceptions
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        assigning the x argument to the right attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        adding the height setter with exceptions
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        task 2:
        assigning the y argument to the right attribute

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        adding the height setter with exceptions
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
