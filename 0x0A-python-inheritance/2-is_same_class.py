#!/usr/bin/python3
"""
function that returns True if the object is exactly an
instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
     is_same_class - returns True if the object is exactly an
                     instance of the specified class ; otherwise False
    args - obj:list object to determing if it is a class
           a_class: the specified class to compare the obj to

    return:True if the object is exactly an instance of the specified
           class,else return False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False


"""
the if statment can also be written simply as
return(type(obj) == a_class)
"""
