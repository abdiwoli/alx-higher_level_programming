#!/usr/bin/python3
def chec(s, v):
    for i in s:
        if (v[0] in i and v[1] in i):
            return True
    return False
arr = []
for v in range(1, 90):
    if v < 9:
       s = "0" + str(v)
    else:
       s = str(v)
    if chec(arr, s):
        continue
    else:
        arr.append(s)
    print(s, end=", ")
print(89)
