#!/usr/bin/python3
def best_score(a=None):
    if a is None or not isinstance(a, dict):
        return None
    if len(a) == 0:
        return None
    arr = [i for i in a.keys()]
    big = arr[0]

    for i in arr[1:]:
        if a[i] > a[big]:
            big = i
    return big
