#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """""
    read_file - reads a text file(UTF8) and prints it to the stdout

    """
    with open(filename, "r", encoding="UTF-8") as my_file:
        read_f = my_file.read()
        print(read_f, end="")
