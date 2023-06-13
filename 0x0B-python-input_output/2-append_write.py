#!/usr/bin/python3
"""
a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    Append_write -   appends a string at the end of a text file (UTF8) and
                     returns the number of characters added

    args  - filename: the name of the file
            text: the text file to append the string to

    return:number of characters added
    """
    with open(filename, 'a', encoding="UTF-8") as my_file:
        return my_file.write(text)
