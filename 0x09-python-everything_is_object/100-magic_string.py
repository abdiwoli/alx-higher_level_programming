#!/usr/bin/python3
def magic_string():
    magic_string.c = 'BestSchool' if not hasattr(magic_string, 'c') else magic_string.c + ', BestSchool'
    return magic_string.c

for i in range(10):
    print(magic_string())
