#!/usr/bin/python3
def best_score(a):
    if a is None:
        return None
    arr = [i for i in a.keys()]
    big = arr[0]

    for i in arr[1:]:
        if a[i] > a[big]:
            big = i
    return big
