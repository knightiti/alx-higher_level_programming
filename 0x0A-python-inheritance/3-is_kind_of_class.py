#!/usr/bin/python3
"""
A function that checks if the object is an instance of a class
 that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """Return true if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
