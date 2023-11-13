#!/usr/bin/python3
""" models/rectangle.py """
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The identifier of the rectangle.
        """
        self.validate(width, "width", 1, "must be > 0")
        self.__width = width
        self.validate(height, "height", 1, "must be > 0")
        self.__height = height
        self.validate(x, "x", 0)
        self.__x = x
        self.validate(y, "y", 0)
        self.__y = y
        super().__init__(id)

    @staticmethod
    def validate(number, name, flag=0, m="must be >= 0"):
        """
        Validate that a number is an integer and satisfies a condition.

        Args:
            number: The number to validate.
            name (str): The name of the property being validated.
            flag (int): The condition the number must satisfy.
            m (str): Additional information about the condition.

        Raises:
            TypeError: If the number is not an integer.
            ValueError: If the number does not satisfy the condition.
        """
        if not isinstance(number, int):
            raise TypeError(f"{name} must be an integer")
        if number < flag:
            raise ValueError(f"{name} {m}")

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.
        """
        self.validate(value, "width", 1, "must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.
        """
        self.validate(value, "height", 1, "must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle's position.

        Args:
            value (int): The new x-coordinate value.
        """
        self.validate(value, "x", 0, "must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The new y-coordinate value.
        """
        self.validate(value, "y", 0, "must be > 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle using '#' characters."""
        print(self.y * "\n", end="")
        for h in range(self.__height):
            print(self.x * " " + self.width * "#")

    def __str__(self):
        """Return a string representation of the rectangle."""
        s = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        s = s + f" - {self.width}/{self.height}"
        return s

    def to_dictionary(self):
        """Convert the rectangle to a dictionary."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """
        Update the rectangle's properties.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            If arguments are provided, update properties accordingly.
            If keyword arguments are provided, update properties using keys.
        """
        if args:
            ln = len(args)
            if ln == 5:
                self.id, self.width, self.height, self.x, self.y = args
            if ln == 4:
                self.id, self.width, self.height, self.x = args
            if ln == 3:
                self.id, self.width, self.height = args
            if ln == 2:
                self.id, self.width = args
            if ln == 1:
                self.id, = args
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
