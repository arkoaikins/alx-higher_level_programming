#!/usr/bin/python3
"""
function that replaces an element in a list at a specific
position without modifying the original list (like in C).
If idx is negative, the function return a copy of the original list
If idx is out of range function return a copy of the original list
"""


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return new_list
    new_list[idx] = element
    return new_list
