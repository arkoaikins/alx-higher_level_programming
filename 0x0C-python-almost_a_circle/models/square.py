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

        """
        task 11
        Update the class Square by adding the public getter and setter size
        """
    @property
    def size(self):
        """ size -  Get size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """
        size -Sets size of the square
        args- value: the value of square's height and width
        """
        self.width = value
        self.height = value

        """task 11 ends here """


        """
        task 12:
        Update the class Square by adding the public method
        def update(self, *args, **kwargs) that assigns attributes
        """

    def update(self, *args, **kwargs):

        """
        update - assigns attributes
        args - *args:list of arguments
               **kwargs: double pointer to a dictionary
        """
        attr = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        """task 12 ends here""






