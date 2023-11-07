#!/usr/bin/python3
"""7-add_item.py"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
my_list = load_from_json_file(filename)
arr = my_list + sys.argv[1:]
print(arr)
save_to_json_file(arr, filename)
