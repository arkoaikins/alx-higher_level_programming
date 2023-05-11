#!/usr/bin/python3
"""
 that imports functions from a file , does some Maths,
 and prints the result
"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    adding = add(a, b)
    minus = sub(a, b)
    multiply = mul(a, b)
    divide = div(a, b)
    print("{} + {} = {}".format(a, b, adding))
    print("{} - {} = {}".format(a, b, minus))
    print("{} * {} = {}".format(a, b, multiply))
    print("{} / {} = {}".format(a, b, divide))
