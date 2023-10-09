#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        n = len(my_list)
        for el in range(n, 0, -1):
            print("{:d}".format(my_list[el]))
