#!/usr/bin/python3
"""
 update_dictionary - replaces or adds key/value in a dictionary.
 @a_dictionary: the dictionary with the key and value
 @key: key of the dictionary
 @value: value of the dictionary
 Return: dictionary that has been modified

"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
