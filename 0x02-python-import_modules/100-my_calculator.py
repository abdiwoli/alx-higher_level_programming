#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = "+-*/"
    if sys.argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exut(1)
    else:
           op = sys.argv[2]
           a = int(sys.argv[1])
           b = int(sys.argv[3])
           if op == "+":
               print("{} + {} = {}".format(a, b, add(a, b)))
           elif op == "-":
               print("{} - {} = {}".format(a, b, sub(a, b)))
           elif op == "*":
               print("{} * {} = {}".format(a, b, mul(a, b)))
           elif op == "/":
               print("{} / {} = {}".format(a, b, div(a, b)))
