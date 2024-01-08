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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """class Sqaure"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
