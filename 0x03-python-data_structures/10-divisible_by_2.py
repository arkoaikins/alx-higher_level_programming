#!/usr/bin/python3
"""
 a function that finds all multiples of 2 in a list.
 Return a new list with True or False, depending on
 whether the integer at the same position in the original
 list is a multiple of 2
 """


def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
