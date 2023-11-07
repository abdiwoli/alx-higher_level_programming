#!/usr/bin/python3
"""import python"""


def append_after(filename="", search_string="", new_string=""):
    """append function"""
    with open(filename, "r") as file:
        lines = []
        append_next_line = False

        for line in file:
            if append_next_line:
                # Append the new string after the next comma
                index = line.find(',')
                if index != -1:
                    line = line[:index + 1] + new_string + line[index + 1:]

                append_next_line = False

            lines.append(line)

            if search_string in line:
                append_next_line = True

    with open(filename, "w") as file:
        file.writelines(lines)
