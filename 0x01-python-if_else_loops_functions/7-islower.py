#!/usr/bin/python3
def islower(s):
    if (s == '' or s is None):
        print("Traceback (most recent call last):")
        exit()
    if 'a' <= s <= 'z':
        return True
    return False
