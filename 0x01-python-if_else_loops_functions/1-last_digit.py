#!/usr/bin/python3
import random
flag = 1
number = random.randint(-10000, 10000)
message = "and is greater than 5"
if number < 6:
    flag = -1
    message = "and is less than 6 and not 0"
if (number == 0):
    message = "and is 0"
str = str(number)
digit = int(str[-1])
digit *= flag
print(f"Last digit of {number} is {digit} {message}")
