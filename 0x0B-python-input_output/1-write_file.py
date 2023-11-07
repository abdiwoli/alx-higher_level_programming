#!/usr/bin/python3
"""importing modules section"""


def write_file(filename="", text=""):
    """function writes to a file and returns the character count"""
    with open(filename, "w") as file:
        return file.write(text)

