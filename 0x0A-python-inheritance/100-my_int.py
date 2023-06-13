#!/usr/bin/python3
"""
 a class MyInt that inherits from in

"""


class MyInt(int):
    """A class MyInt"""
    def __init__(self, value):
        """Instantiazation with a value"""
        self.value = value

    def __eq__(self, other):
        """Invert int operators == """
        return self.value != other

    def __ne__(self, other):
        """Invert int operators !="""
        return self.value == other
