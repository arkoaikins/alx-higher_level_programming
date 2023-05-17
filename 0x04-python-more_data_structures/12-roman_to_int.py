#!/usr/bin/python3
"""

A function that converts a Roman numeral to an integer.
"""
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_letters = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50,
        'X': 10, 'V': 5, 'I': 1
    }
    num = 0
    last = 0

    for letter in roman_string:
        value = roman_letters.get(letter, 0)
        if value == 0:
            continue

        if last == 0 or last >= value:
            num += value
        else:
            num += value - (last * 2)

        last = value

    return num
