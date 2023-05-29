#!/usr/bin/python3
import sys
"""
safe_function - executes a function safely.
@fct: pointer to a function
@args: argument lists
"""


def safe_function(fct, *args):
    try:
        i = fct(*args)
        return i
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
