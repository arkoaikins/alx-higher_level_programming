#!/usr/bin/python3
"""
 function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - Divide all elements of a matrix.
    args: matrix =  list of lists of integers or floats
          div = a number (integer or float)

    Returns: a new matrix
    """
    new_matrix = []

    if not isinstance(div, (int, float)):
        """
        raises type error when div is not a number
        """
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif div == float('inf') or div == float('-inf'):
        raise OverflowError("float overflow")

    if not isinstance(matrix, list):
        """
        raises type error when matrix is not a matrix(list of lists)
        """
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

        list_len = len(matrix[0])
        if list_len != len(item):
            raise TypeError("Each row of the matrix must have the same size")

        for num in item:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    new_matrix = [[round((num / div), 2) for num in row] for row in matrix]
    return (new_matrix)
