#!/usr/bin/python3
"""Defines a class Node"""


class Node:
    """ here we difine class properities"""
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value


class SinglyLinkedList:
    """ here we difine class properities"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            cr = self.__head
            while cr.next_node is not None and cr.next_node.data < value:
                cr = cr.next_node
            new_node.next_node = cr.next_node
            cr.next_node = new_node

    def __str__(self):
        current = self.__head
        elements = []
        while (current is not None):
            elements.append(str(current.data))
            current = current.next_node
        return "\n".join(elements)
