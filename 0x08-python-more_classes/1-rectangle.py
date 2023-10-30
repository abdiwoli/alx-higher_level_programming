#!/usr/bin/python2
"""Class Rectangle define"""


class Rectangle:
    """A class to represent a rectangle with private instance ."""

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        if self.errors(width) and self.errors(height):
            self.__width = width
            self.__height = height

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.
        """
        if self.errors(value):
            self.__height = value

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.
        """
        if self.errors(value):
            self.__width = value

    def errors(self, value):
        """
        Check if the value is a valid integer for width and height.

        This function will print an error message and return False.

        Args:
            value (int): The value to check.

        Returns:
            bool: True if the value is valid, False if it's not.
        """
        if not isinstance(value, int):
            print("Error: Width and height must be integers")
            return False
        elif value < 0:
            print("Error: Width and height must be >= 0")
            return False
        return True
