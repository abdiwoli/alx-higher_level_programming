#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    d = {
        "I": 1, "IV": 4, "IX": 9, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000,
        "i": 1, "iv": 4, "v": 5, "ix": 9, "x": 10,
        "l": 50, "c": 100, "d": 500, "m": 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = d.get(char, 0)

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total
