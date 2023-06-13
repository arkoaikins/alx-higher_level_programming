#!/usr/bin/python3
"""
a class Student that defines a student by:
First_name
Last_name
age
"""


class Student:
    """A class student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialization with first_name,last_name and age attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json - retrieves a dictionary representation of a Student instance

        args - attrs: list of strings, only attribute names contained in this
                      list must be retrieved
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
