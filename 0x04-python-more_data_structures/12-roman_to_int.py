#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {"I": 1, "IV": 4, "IX": 9, "V": 5, "X": 10, "L": 50, "C": 100}
    d.update({"D": 500, "M": 1000})
    d.update({"i": 1, "iv": 4, "v": 5, "ix": 9, "x": 10})
    d.update({"l": 50, "c": 100, "d": 500, "m": 1000})
    values = [i for i in d.keys()]
    if (roman_string in values):
        return d[roman_string]
    s = sum(list(map(lambda x: d[x], roman_string)))
    return s
