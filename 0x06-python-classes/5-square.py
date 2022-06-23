#!/usr/bin/python3
"""module of class containing getter and setter print square"""


class Square():
    """
        size - size of square
    """
    def __init__(self,size=0):
        """init square"""
        self.size=size
    @property
    def size(self):
        """
            int:private size
            Returns:
                Private size
        """
        return self.__size
    
    @size.setter
    def size(self,value):
        """Sets value in size and must be int
            Args:
                value (int): size of squaare
        """
        if (type(value) == int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value <0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        """
            returns the area
            Returns:
                area.
        """
        return(self.__size **2)
    def my_print(self):
        """
            printsthe square with #
        """
        if self.__size == 0:
            print("\n")
        else:
            for item in range(self.__size):                   
                print("#"*self.__size)
