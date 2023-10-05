#!/usr/bin/python3
add = __import__('calculator_1').add
sub = __import__('calculator_1').sub
mul = __import__('calculator_1').mul
div = __import__('calculator_1').div
a = 10
b = 5
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
