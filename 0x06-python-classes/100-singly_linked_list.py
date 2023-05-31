#!/usr/bin/python3
"""
 a class Node that defines a node of a singly linked list by
 Private instance attribute: data
 Private instance attribute: next_node
 Instantiation with data and next_node:
 def __init__(self, data, next_node=None)
"""


class Node:
    """" a class node"""

    def __init__(self, data, next_node=None):
        """ a node with an instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """collects data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """sets data"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Returns size of node instance"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets the next node value"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """a singly linked list is defined"""

    def __init__(self):
        """singly linked list initialization"""

        self.head = None

    def __str__(self):
        """set list to be printed"""

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """
        set a sorted list with the the value to be
        on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
