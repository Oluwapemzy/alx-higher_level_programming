#!/usr/bin/python3
"""moduke contains class which has getter and setter"""


class Square():
    """
        @size - size of square
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
            int:private size
            Returns:
                Private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value in size and must be int
            Args:
                value (int): size of squaare
        """
        if (type(value) == int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
            returns the area
            Returns:
                area.
        """
        return(self.size ** 2)
