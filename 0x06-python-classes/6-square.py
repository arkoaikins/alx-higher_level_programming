#!/usr/bin/python3
"""
 a class Square that defines a square by: (based on 5-square.py)
"""


class Square():
    """a class square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """calculates the square's area and returns it"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets size attribute"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Returns size of Square instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position attribute"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # to stdout"""
        if self.__size <= 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
