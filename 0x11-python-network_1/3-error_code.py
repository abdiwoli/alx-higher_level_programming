#!/usr/bin/python3
""" what is my ip"""
from sys import argv
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as fetch:
            contb = fetch.read()
            conts = contb.decode("ascii")
            print(conts)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
