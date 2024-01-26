#!/usr/bin/python3
""" use requests """
import requests


if __name__ == "__main__":
    fetch = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(fetch)}")
    print(f"\t- content: {fetch.text}")
