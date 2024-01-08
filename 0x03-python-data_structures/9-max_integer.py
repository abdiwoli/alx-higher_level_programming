#!/usr/bin/python3
def max_integer(a=[]):
    if a is None or len(a) == 0:
        return None
    big = a[0]
    for i in a[1:]:
        if (big < i):
            big = i
    return big
