#!/usr/bin/python3
"""
creating a BaseGeometry class with a defined instance
"""


class BaseGeometry:
    """A class with public instance method"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
