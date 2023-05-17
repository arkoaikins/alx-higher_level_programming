#!/usr/bin/python3
"""
A functon that computes the square valuse of all integers of a matrix.
Returns a new matrix,same size as matrix.
Each value is the square of the value of the input.
"""


def square_matrix_simple(matrix=[]):
    new_matrix = [list(map((lambda x: x * x), members)) for members in matrix]
    return new_matrix
