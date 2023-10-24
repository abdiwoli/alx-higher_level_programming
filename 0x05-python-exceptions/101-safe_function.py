#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        if len(args) > 1:
            return fct(args[0], args[1])
        return fct()
    except Exception as e:
        sys.stderr.write("Exception: " + str(e) + "\n")
        return None
