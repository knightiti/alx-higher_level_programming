#!/usr/bin/python3
""" This module defines a class named square and gives it a size attribute """


class Square:
    """
    Represents a class named square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
