#!/usr/bin/python3
"""
function that returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified
class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    inherits_from - returns True if the object is an instance of a class that
                     inherited (directly or indirectly) from the specified
                     class ; otherwise False

     args - obj:  returns True if the object is exactly an
                     instance of the specified class

            a_class:the specified class to compare the obj to
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False


"""
the if statment can also be written simply as
 return(issubclass(type(obj), a_class) and type(obj) != a_class)
"""
