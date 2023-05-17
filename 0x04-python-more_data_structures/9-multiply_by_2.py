#!/usr/bin/python3
"""
multiply_by_2 - function that returns a new dictionary with
                all values multiplied by 2
@a_dictionary: the dictionaly whose values will be multiplied
Return:new_dictionary with elements from a_dictionary  multiplied
"""


def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()

    for key, value in new_dictionary.items():
        new_dictionary[key] = value * 2

    return new_dictionary
