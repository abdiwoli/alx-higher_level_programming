#!/usr/bin/python3
"""module section"""


def add_attribute(obj, attr_name, attr_value):
    """add_attribute function"""
    if not type(obj) == str:
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
