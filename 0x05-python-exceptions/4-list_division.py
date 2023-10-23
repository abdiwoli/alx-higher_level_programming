#!/usr/bin/python3
def list_division(a, b, list_length):
    arr = [0] * list_length
    temp = 0
    for i in range(list_length):
        try:
            temp = a[i] / b[i]
        except ZeroDivisionError:
            print("division by 0")
            temp = 0
        except IndexError:
            print("out of range")
            temp = 0
        except TypeError:
            print("wrong type")
            temp = 0
        finally:
            arr[i] = temp
    return arr
