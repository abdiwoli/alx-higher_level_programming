#!/usr/bin/python3
""" use requests to get variable"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    try:
        print(res.headers['X-Request-Id'])
    except KeyError as e:
        pass
