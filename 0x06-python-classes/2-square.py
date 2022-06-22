#!/usr/bin/python3
"""class that sets size om some conditions"""


class Square():
    """xlass defines size"""
    def __init__(self, size=0):
        """initialoze class Square and sets sizr"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
