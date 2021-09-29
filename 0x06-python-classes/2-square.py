#!/usr/bin/python3
""" This module defines a square with a size validation """


class Square:
    """
    Represents a class named square.
    Private instance attribute: size.
    Instantiation with optional size.
    """

    def __init__(self, size=0):
        """Initializes the size attribute."""
        self.__size = size
        """__size: size of the new square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
