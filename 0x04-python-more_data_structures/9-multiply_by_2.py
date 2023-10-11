#!/usr/bin/python3
def multiply_by_2(a):
    d = dict()
    for i, v in zip(a.keys(), a.values()):
        d[i] = v * 2
    return d

