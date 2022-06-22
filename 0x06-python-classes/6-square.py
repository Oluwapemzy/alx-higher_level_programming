#!/usr/bin/python3
class Square():
    """
        @size - size of square
    """
    def __init__(self,size=0, position=(0, 0)):
        self.size=size
        self.position = position
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
        return(self.size **2)
    def my_print(self):
        """
            prints the square with #
        """
        if self.__size == 0:
            print("\n")
        else:
            for item in range(self.__size):                   
                print(f"{' '*self.__position[0]}{'#'*self.__size}\n")

    @property
    def position(self):
        """Returns position"""
        return self.__position
    @position.setter
    def position(self, value):
        """
        @param: value
        """
        if (type(value)==tuple):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
