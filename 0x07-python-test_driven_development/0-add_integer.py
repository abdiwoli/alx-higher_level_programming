#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result.

    Args:
        a (int or float): The first number.
        b (int or float): The second number (default is 98).

    Returns:
        int: The sum of 'a' and 'b' converted to an integer.

    Raises:
        TypeError: If 'a' or 'b' is not an integer or float.

    Example:
        >>> add_integer(3, 5)
        8

        >>> add_integer(100.3, -2)
        98

        >>> add_integer("hello", 5)
        a must be an integer or float

    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
