#!/usr/bin/python3
"""
A class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    A class BaseGeometry
    """
    def area(self):
        """
        area - that raises an Exception with the message area() is not
               implemented when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator - validates that value

        args- name: The name(always a string)
              value: The value to be validated

        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
