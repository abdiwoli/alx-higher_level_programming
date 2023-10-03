#!/usr/bin/python3
init = 0;
for i in range(0, 99):
    if (i < 10):
        init = 0
    else:
        init = ""
    print("{0}{1}, ".format(init, i), end="");
print(99);
