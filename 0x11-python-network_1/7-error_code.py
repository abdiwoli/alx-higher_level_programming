#!/usr/bin/python3
""" what is my ip"""
from sys import argv
import requests

if __name__ == "__main__":
    fetch = requests.get(argv[1])
    if fetch.status_code // 100 == 2:
        print(fetch.text)
    else:
        print("Error code: {}".format(fetch.status_code))
