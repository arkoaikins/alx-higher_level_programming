#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file
"""

import json
""" importing the json module"""


def load_from_json_file(filename):
    """
    load_from_json_file - creates an Object from a “JSON file”

    """
    with open(filename, 'r', encoding='UTF-8') as my_file:
        return json.load(my_file)
