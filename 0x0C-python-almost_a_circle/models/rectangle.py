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
