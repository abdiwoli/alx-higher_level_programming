#!/usr/bin/python3
"""Module containing is_same_class method"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    This function takes an object `obj` and a class `a_class` as parameters. It checks if the type of the object `obj` matches the class `a_class`.

    Args:
        obj: The object to be checked.
        a_class: The class to compare the object's type to.

    Returns:
        bool: True if the object is an instance of the specified class; False otherwise.

    Example:
        >>> a = 1
        >>> is_same_class(a, int)
        True

    """
    return type(obj) is a_class
