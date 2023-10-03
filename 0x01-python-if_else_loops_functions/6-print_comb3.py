#!/usr/bin/python3
def chec(v):
    if (int(v) < 10):
        return False
    if (int(v[1] + v[0]) > int(v)):
        return True
    return False

for v in range(1, 90):
    if v < 10:
       s = "0" + str(v)
    else:
       s = str(v)
    if chec(s):
        continue
    print("{0}".format(s), end=", ")
print(89)
