#!/usr/bin/python3
def print_sorted_dictionary(d):
    k = sorted(d.keys())
    for i in k:
        print("{}: {}".format(i, d[i]))
