#!/usr/bin/python3
def print_last_digit(number):
    flag = 1
    if number < 0:
        number = number * -1
        flag = -1
    if number > 9:
        number = number % 10
    print(number, end="")
    return (number);
