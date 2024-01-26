#!/usr/bin/python3
""" what is my ip"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as fetch:
        contb = fetch.read()
        conts = contb.decode("utf-8")
        print(counts)
