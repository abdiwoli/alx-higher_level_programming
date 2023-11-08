#!/usr/bin/python3
"""import python"""


def append_after(filename="", search_string="", new_string=""):
    """append function"""
    with open(filename, "r") as file:
        lines = []
        a = True
        
        for line in file:
            if search_string in line and a:
                lines.append(line)
                lines.append(new_string)
            else:
                lines.append(line)                

    with open(filename, "w") as file:
        file.writelines(lines)
