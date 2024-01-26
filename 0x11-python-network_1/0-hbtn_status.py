#!/usr/bin/python3
""" what is my ip"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as fetch:
        contb = fetch.read()
        conts = contb.decode("utf-8")
        print("Body response:")
        print(f"    - type: {type(contb)}")
        print(f"    - content: {contb}")
        print(f"    - utf8 content: {conts}")
