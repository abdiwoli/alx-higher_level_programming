#!/usr/bin/python3
def search_replace(my_list, search, replace):
    arr = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            arr.append(replace)
        else:
            arr.append(my_list[i])
    return arr
