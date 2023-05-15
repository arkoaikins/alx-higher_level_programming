#!/usr/bin/python3
"""
a function that adds 2 tuples.
Returns a tuple with 2 integers
The first element is the addition of the first element of each argument
The second element is the addition of the second element of each argument
"""


def add_tuple(tuple_a=(), tuple_b=()):
    listc_1 = [tuple_a[i] if i < len(tuple_a) else 0 for i in range(2)]
    listc_2 = [tuple_b[i] if i < len(tuple_b) else 0 for i in range(2)]
    sum_0 = listc_1[0] + listc_2[0]
    sum_1 = listc_1[1] + listc_2[1]
    new_tuple = (sum_0, sum_1)
    return new_tuple
