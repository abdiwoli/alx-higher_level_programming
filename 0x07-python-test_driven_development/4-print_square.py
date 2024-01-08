#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int) or isinstance(size, bool) or size < 0:
        raise TypeError("size must be an integer") if not isinstance(size, int) else ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

