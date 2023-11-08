#!/usr/bin/python3
"""10-square.py"""
Rectangle = __import__('9-rectangle').Rectangle


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


class Square(Rectangle):
    """class Sqaure"""
    def __init__(self, size):
        super().__init__()
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
