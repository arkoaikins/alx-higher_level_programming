#!/usr/bin/python3
import json
import turtle
import csv

"""
Createing a  class which will be the “base” of all other classes
in this project.The goal of it is to manage id attribute in all
classes and to avoid duplicatingthe same code (by extension, same bugs)
"""


class Base:
    """
    A class Base for all the classes
    with a private class attribute
    """
    __nd_objects = 0

    def __init__(self, id=None):
        """
        Initialization with id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects
