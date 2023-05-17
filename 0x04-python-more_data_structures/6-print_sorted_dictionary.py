#!/usr/bin/python3
"""
print_sorted_dictionary - prints a dictionary by ordered keys.
@a_dictionary
Return: sorted keys
"""


def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items())
    for key, value in sorted_dict:
        print("{}: {}".format(key, value))
