#!/usr/bin/python3
"""Defines a class MagicClass"""


class MagicClass:
    """ here we difine class properities"""
    def __init__(self, radius=0):
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        import math
        return math.pi * self.__radius ** 2

    def circumference(self):
        import math
        return 2 * math.pi * self.__radius
