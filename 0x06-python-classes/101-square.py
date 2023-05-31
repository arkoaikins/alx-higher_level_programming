#!/usr/bin/python3
"""Square module"""


class Square():
    """ a class square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns size of Square"""
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
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size, end="")
            # to not print newline after square is printed
            if _ < self.__size - 1:
                print()

    def __str__(self):
        """
        makes square work same as my_print()
        """
        self.my_print()
        return ""
