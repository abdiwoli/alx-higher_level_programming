#!/usr/bin/python3
def magic_string():
    if "count" not in magic_string.__dict__:
        magic_string.count = "BestSchool"
    magic_string.count += ", BestSchool"
    return (magic_string.count)
