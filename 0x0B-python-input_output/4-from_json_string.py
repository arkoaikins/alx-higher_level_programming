#!/usr/bin/python3
"""
a function that returns an object (Python data structure)
represented by a JSON string:
"""

import json
""" importing the json module"""


def from_json_string(my_str):
    """
    to_json_string - returns an object (Python data structure)
                     represented by a JSON string
    args - my_str: The json string

    return:an object (Python data structure)
           represented by a JSON string
    """
    return json.loads(my_str)
