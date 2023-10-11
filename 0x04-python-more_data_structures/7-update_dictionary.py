#!/usr/bin/python3
def update_dictionary(a, key, value):
    a.get(key, value)
    a[key] = value
    return a

