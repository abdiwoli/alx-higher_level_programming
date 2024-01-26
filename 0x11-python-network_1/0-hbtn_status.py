#!/usr/bin/python3
""" what is my ip"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as fetch:
        contb = fetch.read()
        conts = contb.decode("utf-8")
        print("Body response:")
        print(f"\t- type: {type(contb)}")
        print(f"\t- content: {contb}")
        print(f"\t- utf8 content: {conts}")
