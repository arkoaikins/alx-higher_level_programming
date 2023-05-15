#!/usr/bin/python3
"""
function that removes all characters c and C from a string.
"""


def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new_string += c
    return new_string
