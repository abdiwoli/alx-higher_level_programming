#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()

n = len(sys.argv) - 1
if n == 1:
    m = f"1 argument:"
elif n == 0:
    m = "0 arguments."
else:
    m = "{} arguments:".format(n)
print(m)
i = 1
for j, i in enumerate(range(1, n)):
    print("{}: {}".format(j + 1, sys.argv[i]))
if n > 0:
    print("{}: {}".format(n, sys.argv[n]))
