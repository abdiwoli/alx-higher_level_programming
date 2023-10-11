#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    d.update({"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000})
    s = sum(list(map(lambda x: d[x], roman_string)))
    return s
