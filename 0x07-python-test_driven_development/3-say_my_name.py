#!/usr/bin/python3
"""
a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name="", last_name=""):
    """
    say_my_name -  prints My name is <first name> <last name>
    args:first_name: the first name
         last_name: the last name
    return: name
    """
    if not isinstance(first_name, str) or not first_name:
        """
        raises type error if first name is not a string
        """
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        """
        raises type error if last name is not a string
        """
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
