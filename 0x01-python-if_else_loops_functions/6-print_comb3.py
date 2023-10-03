#!/usr/bin/python3
def chec(v):
    if int(v) < 10:
        return False
    return sorted(v) == list(v)

for i in range(10):
    for j in range(i + 1, 10):
        s = f"{i}{j}"
        if chec(s) or j < 10:
            print("{0}".format(s), end=", ")

print()
