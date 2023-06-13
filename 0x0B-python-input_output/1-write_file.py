#!/usr/bin/python3
"""Defines a write_file() method"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    Args:
        filename: name of file
        text: string to be written
    Return:
        number of characters written
    """
    with open(filename, 'w', encoding="UTF-8") as my_file:
        return my_file.write(text)
