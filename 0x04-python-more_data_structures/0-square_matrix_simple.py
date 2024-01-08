#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    n = len(matrix)

    for i in range(n):
        h = len(matrix[i])
        arr = []
        for j in range(h):
            arr.append(matrix[i][j] ** 2)
        new_m.append(arr)
    return new_m
