#!/usr/bin/python3
"""
 a function def pascal_triangle(n): that returns a list of lists of integers
 representing the Pascal’s triangle of n

"""


def pascal_triangle(n):
    """
    pascal_triangle - returns a list of lists of integers representing
                      the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trian = triangles[-1]
        temp = [1]
        for pa_tr in range(len(trian) - 1):
            temp.append(trian[pa_tr] + trian[pa_tr + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
