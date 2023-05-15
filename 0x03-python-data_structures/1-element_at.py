#!/usr/bin/python3
"""
function that retrieves an element from a list like in C.
if idx is negative,function returns None
if idx is out of range,function returns None
"""


def element_at(my_list, idx):
    if 0 >= idx > len(my_list):
        return None
    return my_list[idx]
