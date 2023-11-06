#!/usr/bin/python3
""" import module"""


def lookup(obj):
    """ function lookup

    Args:
        obj: object

    Return:
        return: list
     """
    return [i for i in obj.__dict__]
