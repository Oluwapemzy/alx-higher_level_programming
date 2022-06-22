#!/usr/bin/python3
"""module that contains a class that sets size and finds area"""


class Square():
    """sets size and jas methid area"""
    def __init__(self, size=0):
        """sets size on condition"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """finds area of dquare """
        return (self.__size ** 2)
