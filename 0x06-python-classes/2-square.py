#!/usr/bin/python3
"""
class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    def __init__(self, size=0):
        """instantiation with optional"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        """raises type error exception with a message"""
        if size < 0:
            raise ValueError("size must be >= 0")
        """raises valueerror exception with a message"""
        self.__size = size
