#!/usr/bin/python3
def manage(a):
	n = len(a)
	while (len(a) < 2):
		if n == 0:
			a = (0, 0)
		else:
			a = (a[0], 0)
	return a


def add_tuple(a=(),  b=()):
	a = manage(a)
	b = manage(b)
	return (a[0] + b[0], a[1] + b[1])

