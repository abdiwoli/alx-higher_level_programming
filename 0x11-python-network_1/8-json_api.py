#!/usr/bin/python3
""" post request with paramater """
from sys import argv
import requests


def send_post(q):
    data = {'q': q}
    res = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        jsn = res.json()
        if len(jsn) == 0:
            print("No result")
        else:
            print("[{}] {}".format(jsn.get("id"), jsn.get("name")))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
        send_post(q)
    else:
        print("No result")
