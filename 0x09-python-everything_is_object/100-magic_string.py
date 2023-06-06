#!/usr/bin/python3
def magic_string():
    magic_string.iterate = getattr(magic_string, 'iterate', 0) + 1
    return ("BestSchool, " * (magic_string.iterate - 1) + "BestSchool")
