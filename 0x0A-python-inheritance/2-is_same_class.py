#!/usr/bin/python3
"""
A function that checks the exact instance of a specified class
"""


def is_same_class(obj, a_class):
    """Return true if the object is the exact instance of a_class,
 otherwise false"""
    return (type(obj) == a_class)

