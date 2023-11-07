#!/usr/bin/python3
"""importing modules section"""


def read_file(filename=""):
    """function reads file"""
    with open(filename, "r") as file:
        for line in file:
            print(line)
