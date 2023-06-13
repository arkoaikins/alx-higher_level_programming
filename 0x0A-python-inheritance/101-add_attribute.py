#!/usr/bin/python3
"""
a function that adds a new attribute to an object if it’s possible

"""


def add_attribute(obj, attr, value):
    """
    adds attribute - adds a new attribute to an object if it’s possible
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
