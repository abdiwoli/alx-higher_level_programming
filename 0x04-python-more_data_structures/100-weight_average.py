#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    av = 0
    arr = [i[1] for i in my_list]
    for i in my_list:
        av += i[0] * i[1]
    return av / sum(arr)
