#!/usr/bin/python3
""" post request with paramater """
from sys import argv
from urllib import request, parse


def send_post(url, email):
    d = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(url, d) as resp:
        response = resp.read().decode("utf-8")
        print(response)


if __name__ == "__main__":
    send_post(argv[1], argv[2])
