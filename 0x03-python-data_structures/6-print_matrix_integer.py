#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        n = len(i) - 1
        for v, j in enumerate(i):
            t = " " if v < n else ""
            print("{}".format(j), end=t)
        print()
