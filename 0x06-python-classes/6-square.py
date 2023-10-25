#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ here we difine class properities"""
    def __init__(self, size=0, pos=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(pos, tuple) or not pos[1] or not op[0]:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = pos

    def area(self):
        return self.__size ** 2

    def my_print(self):
        sz = self.__size
        if (sz == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(sz):
                sp = " " * self.__position[0]
                print(sp + "#" * sz)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def postion(self, value):
        if not isinstance(pos, tuple) or pos[0] < 0 or pos[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value
