#!/usr/bin/python3
"""
a function that returns the JSON representation of an object (string)
"""
import json
""" importing the json module"""


def to_json_string(my_obj):
    """
    to_json_string - returns the JSON representation of an object (string)
    args - my_obj: object to be serialized

    return:the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
