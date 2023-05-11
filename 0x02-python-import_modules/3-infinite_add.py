#!/usr/bin/python3
"""
 program that displays the result of the addition of all arguments
"""

if __name__ == "__main__":
    from sys import argv
    sum = 0
    for i in argv[1:]:
        sum += int(i)
    print("{}".format(sum))
