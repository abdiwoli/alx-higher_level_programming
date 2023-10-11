#!/usr/bin/python3
import sys
n = len(sys.argv) - 1
if __name__ != "__main__":
    exut()
sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])
if n > 0:
    sum += int(sys.argv[n])
print("{}".format(sum))
