#!/usr/bin/python3
""" post request with paramater """
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


def get_id(user, passw):
    url = "https://api.github.com/user"
    res = requests.get(url, auth=HTTPBasicAuth(user, passw))
    print(res.json().get("id"))


if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    get_id(user, passw)
