#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers
    Returns: peak of list_of_integers found or None
    """
    size = len(list_of_integers)
    mid_e = size
    peak = size // 2

    if size == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (peak < size - 1 and
                list_of_integers[peak] < list_of_integers[peak + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            peak = peak + mid_e // 2
        elif mid_e > 0 and list_of_integers[peak] < list_of_integers[peak - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            peak = peak - mid_e // 2
        else:
            return list_of_integers[peak]
