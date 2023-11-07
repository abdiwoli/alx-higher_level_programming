#!/usr/bin/python3
"""importing modules section"""


def write_file(filename="", text=""):
    """function writes to a file and returns the character count"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
