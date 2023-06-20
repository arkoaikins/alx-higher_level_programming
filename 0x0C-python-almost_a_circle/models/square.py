#!/usr/bin/python3
"""
Create class square
class Square that inherits from the Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square inheriting from the rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        task 10:
         __init__ - initialization with size,x,y and id attributes
        """
        super().__init__(size, size, x, y, id)

        """
        Calling the super class with id,x,y,width and height
        width and height is assigned to the value size
        """

    def __str__(self) -> str:
        """
        Returns string representation of Rectangle instance
        Note that width and height are equal for a Square object
        """
        str_retrns = "[{}] ({}) {}/{} - {}"
        id_d = self.id
        x_x = self.x
        y_y = self.y
        w = self.width
        return str_retrns.format(__class__.__name__, id_d, x_x, y_y, w)
        """
        task 10 ends here
        """
