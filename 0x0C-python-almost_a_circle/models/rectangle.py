#!/usr/bin/python3
"""module of class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle""" 
    def __init__(self, width, height, x=0, y=0, id=None): 
        """Init function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width function"""
        return self.__width

    @property
    def height(self):
        """get height func"""
        return self.__height

    @property
    def x(self):
        """x func"""
        return self.__x
    
    @property
    def y(self):
        """get_y funct"""
        return self.__y

    @width.setter
    def width(self, width):
        """set_width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width


    @height.setter
    def height(self, height):
        """set_height funct"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """set_x funct"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x


    @y.setter
    def y(self, y):
        """set_y function"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns area of Rectangle"""
        return (self.height * self.width)

    def display(self):
        """Display rectangle"""

        if self.__y !=0:
            for newline in range(self.y):
                print()
        for num in range(self.height):
            print((self.x * " ") + (self.width * '#'))

    def __str__(self):
        """__str__ method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update using *args"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self,key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle"""
        dict_rep = {'x': self.x, 'width': self.__width, 'id':self.id, 'height': self.__height, 'y':self.y}
        return dict_rep
