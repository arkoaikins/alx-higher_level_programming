#!/usr/bin/python3
"""
multiply_list_map - function that returns a list with all
                   values multiplied by a number without using any loops.
@my_list=[]:list with elements in them
@ number: the multiplier of each value in the list
Return:list with all values multiplied by a number without using any loops.
"""


def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda x: x * number, my_list))
    return new_list
