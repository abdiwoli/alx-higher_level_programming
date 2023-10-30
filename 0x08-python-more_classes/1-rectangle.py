#!/usr/bin/python3
"""class Rectngle atributes
"""


class Rectangle:
    """class Rectngle atributes
     """

    def __init__(self, width=0, height=0):
        self.errors(width)
        self.errors(height)
        self.__width = width
        self.__height = height

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, value):
        self.errors(value)
        self.__height = value

    @property
    def width(self):
        return self.__width

    @height.setter
    def width(self, value):
        self.errors(value)
        self.__width = value

    def errors(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
