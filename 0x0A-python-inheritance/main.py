#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = 39
add_attribute(mc, "name", "John")
print(mc.name)
