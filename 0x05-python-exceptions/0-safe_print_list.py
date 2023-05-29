#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i, lists in enumerate(my_list):
        if counter == x:
            break
        try:
            print(lists, end="")
            counter += 1
        except Exception as e:
            pass
    print()
    return counter
