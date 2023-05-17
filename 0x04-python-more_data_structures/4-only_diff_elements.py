#!/usr/bin/python3
"""
only_diff_elements - print  a set of all elements present in only one set.
@set_1: The first set
@set_2: The second set
Return: a set with all the elements in only one set
"""


def only_diff_elements(set_1, set_2):
    all_elements = set_1.symmetric_difference(set_2)
    return all_elements
