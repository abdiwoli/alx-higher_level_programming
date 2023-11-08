#!/usr/bin/python3
Square = __import__('10-square').Square
Rectangle = __import__('9-rectangle').Rectangle
s = Square(4)
print(issubclass(Square, Rectangle))
print(Square)
print(Rectangle)
