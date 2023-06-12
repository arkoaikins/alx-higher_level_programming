#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """"
    lookup - returns the list of available attributes and methods of an object
    args:obj - the list object that will be retured

    """
    return dir(obj)
