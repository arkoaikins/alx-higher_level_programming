#!/usr/bin/python3
"""
simple_delete - a function that deletes a key in a dictionary.
@a_dictionary:The dictionary
@key="": key of the dictionary
Return: modified dictionary with  deleted key
"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
