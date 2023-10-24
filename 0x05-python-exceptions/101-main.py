#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function


def print_message(a, b):
    print("Hello")

result = safe_function(print_message, 10, 20)
print(result)
