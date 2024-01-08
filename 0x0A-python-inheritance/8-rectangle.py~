#!/usr/bin/python3
"""
===========================
modules
==========================
"""


class BaseGeometry:
    """document BaseGeometry"""

    def area(self):
        """aread public method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is int and value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
