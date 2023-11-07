#!/usr/bin/python3
"""def class_to_json(obj):"""


def class_to_json(obj):
    """class to json"""
    json_dict = {}
    for k, v in obj.__dict__.items():
        if isinstance(v, (str, int, bool, list, dict)):
            json_dict[k] = v
    return json_dict
