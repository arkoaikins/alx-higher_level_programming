#!/usr/bin/python3
"""
A function that writes an Object to a text file, using a JSON representation
"""
import json
""" importing the json module"""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file-  writes an Object to a text file, using a
                        JSON representation
    args - my_obj: object to be serialized
        filename: Text file that object will be written to
    """
    with open(filename, 'w', encoding="UTF-8") as my_file:
        json.dump(my_obj, my_file)
