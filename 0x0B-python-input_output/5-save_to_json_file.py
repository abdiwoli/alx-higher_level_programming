#!/usr/bin/python3
"""import module"""
import json


def save_to_json_file(my_obj, filename):
    """function writes tow file"""
    with open(filename, "w", endcode=encoding="utf-8") as file:
        json.dump(my_obj, file, ensure_ascii=False)
