#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of
an object
"""


def class_to_json(obj):
    """
    class_to_json - returns the dictionary description with simple data
                   structure (list, dictionary, string, integer and boolean)
                   for JSON serialization of an object

    args: obj - an instance of a Class
    """
    return obj.__dict__
