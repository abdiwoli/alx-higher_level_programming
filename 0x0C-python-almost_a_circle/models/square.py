#!/usr/bin/python3
""" models/square.py """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ init function """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size property"""

        return self.width

    @size.setter
    def size(self, size):
        """ setter function """

        self.width = size
        self.height = size

    def __str__(self):
        """ return str """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"

    def update(self, *args, **kwargs):
        """ update function """

        if args:
            if len(args) == 4:
                self.id, self.size, self.x, self.y = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 1:
                self.id, = args
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return function """

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
