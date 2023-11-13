#!/usr/bin/python3
"""
 models/rectangle.py
"""
from models.base import Base


class Rectangle(Base):
    """ class  Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init class """

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
        if not isinstance(number, int):
            raise TypeError(f"{name} must be an integer")
        if number < flag:
            raise ValueError(f"{name} {m}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate(value, "width", 1, "must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate(value, "height", 1, "must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate(value, "x", 0, "must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate(value, "y", 0, "must be > 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        print(self.y * "\n", end="")
        for h in range(self.__height):
            print(self.x * " " + self.width * "#")

    def __str__(self):
        s = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        s = s + f" - {self.width}/{self.height}"
        return s

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }

    def update(self, *args, **kwargs):
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
