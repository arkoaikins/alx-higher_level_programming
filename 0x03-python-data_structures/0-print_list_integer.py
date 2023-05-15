#!/usr/bin/python3
"""
function that prints all integers of a list
displays one integer per line
"""


def print_list_integer(my_list=[]):
    for integers in my_list:
        print("{:d}".format(integers))
