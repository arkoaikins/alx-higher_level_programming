#!/usr/bin/python3
"""
program that displays the number of and the list of its arguments.
"""

if __name__ == "__main__":
    from sys import argv
    counter = len(argv)
    # when no argument is passed
    if counter == 1:
        print("{} arguments.".format(counter - 1))
    # when 1 argument is passed
    elif counter == 2:
        print("{} argument:".format(counter - 1))
    # when more than 1 argument is passed
    else:
        print("{} arguments:".format(counter - 1))
    # display number of argument and argument name
    for i in range(1, counter):
        print("{}: {}".format(i, argv[i]))
