#!/usr/bin/python3
"""
Creating a sub class 'MyList' that inherits 
from class 'list'.
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
A public instance method that prints the list
sorted in ascending order"""
        print(sorted(self))
