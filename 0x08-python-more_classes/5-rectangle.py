#!/usr/bin/python3
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
        if self.errors(width, "width") and self.errors(height, "height"):
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
        if self.errors(value, "height"):
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
        if self.errors(value, "width"):
            self.__width = value

    def errors(self, value, v):
        """
        Check if the value is a valid integer for width and height.

        This function will print an error message and return False.

        Args:
            value (int): The value to check.

        Returns:
            bool: True if the value is valid, False if it's not.

        Raise:
            TypeError: width must be an integer
            ValueError: must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(v))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(v))
        return True

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        s = ""
        if self.__width == 0:
            return ""
        for i in range(self.__height):
            for h in range(self.width):
                s += "#"
            if (i != self.__height - 1):
                s += "\n"
        return s

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
