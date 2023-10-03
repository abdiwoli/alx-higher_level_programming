#!/usr/bin/python3
def islower(s):
    for char in s:
        if 'A' <= char <= 'Z':
            return False
    return True
