#!/usr/bin/python3
"""
imports all functions from the file calculator_1.py
and handles basic operations.
"""

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operations = ["+", "-", "*", "/"]
    functn = [add, sub, mul, div]
    for i, s in enumerate(operations):
        if argv[2] == s:
            print("{} {} {} = {}".format(a, s, b, functn[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
