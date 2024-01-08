#!/usr/bin/python3
"""module section"""


def add_attribute(obj, attr_name, attr_value):
    """add_attribute function"""
    slots = getattr(obj.__class__, '__slots__', None)
    al = (int, str, dict, list, tuple)
    if isinstance(obj, al) or slots is not None and attr_name not in slots:
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
