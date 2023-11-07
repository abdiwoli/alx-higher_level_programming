#!/usr/bin/python3
"""importing modules section"""


def append_write(filename="", text=""):
    """function writes to a file and returns the character count"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
