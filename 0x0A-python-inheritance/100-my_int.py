#!/usr/bin/python3
"""modules"""


class MyInt(int):
    """class Myint"""
    def __eq__(self, other):
        if isinstance(other, int):
            return self == int
        return False

    def __ne__(self, other):
        if isinstance(other, int):
            return not (self == other)
