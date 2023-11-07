#!/usr/bin/python3
"""importing modules section"""


def read_file(filename=""):
    """function reads file"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
