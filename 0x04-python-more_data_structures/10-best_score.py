#!/usr/bin/python3
"""
best_score - function that returns a key with the biggest integer value
@a_dictionary - the dictionary on which the highest value is going to be
                determined
Return:None if no score,else return key with highest value

"""


def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    high_score = max(a_dictionary.values(), default=None)
    for key, value in a_dictionary.items():
        if value == high_score:
            return key
