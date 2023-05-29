#!/usr/bin/python3
"""
list_division - divides element by element 2 lists.
@my_list_1:contain any data type(integer,string etc)
@my_list_2: contain any data type(integer,string etc)
@list_length: can be bigger than the length of both lists
Return: a new list (length = list_length) with all divisions
"""


def list_division(my_list_1, my_list_2, list_length):
    new_l = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('wrong type')
            result = 0
        except ZeroDivisionError:
            print('division by 0')
            result = 0
        except IndexError:
            print('out of range')
            result = 0
        finally:
            new_l.append(result)
    return new_l
