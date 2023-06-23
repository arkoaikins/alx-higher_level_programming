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
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
