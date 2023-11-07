#!/usr/bin/python3
def add_attribute(obj, attr_name, attr_value):
    """add_attribute function"""
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
