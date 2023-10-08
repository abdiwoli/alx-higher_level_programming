#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_arr = []
    n = len(my_list)
    for i in range(n):
        if i == idx:
            new_arr.append(element)
        else:
            new_arr.append(my_list[i])
    return new_arr

