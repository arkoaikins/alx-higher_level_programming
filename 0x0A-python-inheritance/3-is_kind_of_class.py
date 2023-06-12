#!/usr/bin/python3
"""
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - returns True if the object is an instance of,
                       or if the object is an instance of a class that
                       inherited from,the specified class ; otherwise False

    args - obj: object to determine if it is an instance of a class that
                inherited from a specified class

        a_class: the specified class to compare the obj to
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False


"""
the if statment can also be written simply as
return(isinstance(obj, a_class))
"""
