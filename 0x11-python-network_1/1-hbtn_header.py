#!/usr/bin/python3
""" variable value"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as fetch:
        var = fetch.getheader("X-Request-Id")
        print(var)
