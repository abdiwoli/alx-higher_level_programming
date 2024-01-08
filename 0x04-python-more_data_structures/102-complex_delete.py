#!/usr/bin/python3
def complex_delete(d, value):
    if d is None:
        return None
    k = [i for i, v in d.items() if v == value]
    for i in k:
        del d[i]
    return d
