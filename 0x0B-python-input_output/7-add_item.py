#!/usr/bin/python3
"""7-add_item.py"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    arr = load_from_json_file(filename)
except Exception as e:
    arr = []
arr += sys.argv[1:]
save_to_json_file(arr, filename)
