#!/usr/bin/python3
"""
safe_print_division - divides 2 integers
@a:first integer
@b:Second integer
"""
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return 
