#!/usr/bin/python3
def remove_char_at(str, n):
    copy_str = ""
    for i, v in enumerate(str):
        if (i == n):
            continue
        copy_str += v
    return copy_str
