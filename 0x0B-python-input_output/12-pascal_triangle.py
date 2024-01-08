#!/usr/bin/python3
"""file"""


def pascal_triangle(n):
    """function"""
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Compute the next row based on the previous row
        previous_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_value = previous_row[j - 1] + previous_row[j]
            new_row.append(new_value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
