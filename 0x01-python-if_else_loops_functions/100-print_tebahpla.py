#!/usr/bin/python3

"""
program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
"""


for alpha in range(122, 96, -1):
    if alpha % 2 != 0:
        alpha = alpha - 32
    print("{}".format(chr(alpha)), end="")
