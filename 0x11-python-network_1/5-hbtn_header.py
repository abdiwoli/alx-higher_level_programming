#!/usr/bin/python3
""" use requests to get variable"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers['X-Request-Id'])
