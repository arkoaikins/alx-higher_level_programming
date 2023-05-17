#!/usr/bin/python3
"""
a function that deletes keys with a specific value in a dictionary.

"""
def complex_delete(a_dictionary, value):
    key = []
    for i, j in a_dictionary.items():
        if j == value:
            key.append(i)

    for i in key:
        del a_dictionary[i]
    return a_dictionary
