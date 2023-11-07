#!/usr/bin/python3
"""importing modules section"""


def read_file(filename=""):
    """Reads a file and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
