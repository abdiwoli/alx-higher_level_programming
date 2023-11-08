#!/usr/bin/python3
"""module section"""


def add_attribute(obj, attr_name, attr_value):
    """add_attribute function"""
    al = (str, int, float, list, dict)
    if isinstance(obj, al) or attr_name not in obj.__slots__:
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
