#!/usr/bin/python3
"""import python"""


def append_after(filename="", search_string="", new_string=""):
    """append function"""
    with open(filename, "r") as file:
        lines = []
        for line in file:
            if search_string in line:
                lines.append(line)
                lines.append(new_string)
            else:
                lines.append(line)                

    with open(filename, "w") as file:
        file.writelines(lines)
