#!/usr/bin/python3
import sys
"""
safe_print_integer_err - prints an integer.
@value: can be any type (integer, string, etc.)
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return False
