#!/usr/bin/python3
"""
a function that adds all unique integers in
a list (only once for each integer).
Return: sum of all unique intergers
"""


def uniq_add(my_list=[]):
    sum_of_int = sum(set(my_list))
    return sum_of_int
