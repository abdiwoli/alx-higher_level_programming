#!/usr/bin/python3
"""Defines a class MagicClass"""

import dis
class MagicClass:
    """ here we difine class properities"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
