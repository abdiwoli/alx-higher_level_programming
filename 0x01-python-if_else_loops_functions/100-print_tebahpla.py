#!/usr/bin/python3
n = 0
for i in "zyxwvutsrqponmlkjihgfedcba":
    if (n % 2 == 1):
        i = chr(ord(i) - ord('a') + ord('A'))
    print("{0}".format(i), end="")
    n += 1

        
