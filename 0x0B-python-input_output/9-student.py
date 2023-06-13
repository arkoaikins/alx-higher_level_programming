#!/usr/bin/python3
"""
a class Student that defines a student by:
First name
last name
age
"""


class Student:
    """A class student"""
    def __init__(self, first_name, last_name, age):
        """Initialization with first_name,last_name and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary description with simple data structure"""
        return self.__dict__
