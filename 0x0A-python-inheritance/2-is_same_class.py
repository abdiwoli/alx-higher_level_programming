#!/usr/bin/python3
"""Module containing is_same_class method"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: The object to be checked.
        a_class: The class to compare the object's type to.

    Returns:
        bool: True or False

    Example:
        >>> a = 1
        >>> is_same_class(a, int)
        True

    """
    return type(obj) is a_class
