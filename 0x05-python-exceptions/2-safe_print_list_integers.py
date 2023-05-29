#!/usr/bin/python3
"""
 safe_print_list_integers- a function that prints the first x
                           elements of a list and only integers.
 @my_list:list of integers
 Return:the real number of integers printed

 """


def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return counter
