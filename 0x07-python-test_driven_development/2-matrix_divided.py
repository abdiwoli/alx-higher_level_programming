#!/usr/bin/python3
""" module doc"""


def matrix_divided(matrix, div):
    """
    function devides matrix

    Args:
        matrix: lis of list
        div: number

    Return:
        new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    m = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(m)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(m)
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return new_matrix
