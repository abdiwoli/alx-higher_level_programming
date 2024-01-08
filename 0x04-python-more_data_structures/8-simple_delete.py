#!/usr/bin/python3
def simple_delete(a, key=""):
    k = a.keys()
    if key not in k:
        return a
    del a[key]
    return a
