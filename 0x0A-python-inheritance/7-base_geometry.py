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
            raise TypeError(f"{name} must be an 
