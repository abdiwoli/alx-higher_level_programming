#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ here we difine class properities"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        sz = self.__size
        if (sz == 0):
            print()
        else:
            for i in range(sz):
                print("#" * sz)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value
