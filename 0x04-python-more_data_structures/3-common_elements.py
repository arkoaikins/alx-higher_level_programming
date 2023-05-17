#!/usr/bin/python3
"""
Common_elements - Print common element in the set
@set_1 : first set
@set_2: Second set
Returns : common elements in the two sets
"""


def common_elements(set_1, set_2):
    common_ele = set_1.intersection(set_2)
    return common_ele
