#!/usr/bin/python3
"""
a function that replaces all occurrences of an element by another in a new list.
my_list: is the initial list
Search: is the element to replace in the list
Replace: is the new element
Return: new list of the replaced items
"""


def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for new in range(len(new_list)):
        if new_list[new] == search:
            new_list[new] = replace
    return new_list
