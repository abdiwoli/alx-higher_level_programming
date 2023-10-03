#!/usr/bin/python3
n = 0;
for i in "zyxwvtsrqponmlkjhgfedcba":
    if (n % 2 == 1):
        i = chr(ord(i) - ord('a') + ord('A'))
    print("{0}{1}".format(i, "\n" if i == "A" else ""), end="")
    n += 1

        
