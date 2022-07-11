#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """a  class Square which inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the Square classs"""
        self.size = size
        super().__init__(width=size, height=size, x=x, y=y,id=id)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.size}")
    @property
    def size(self):
        """Retrieves the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """update the Square class using *args and **kwargs
            Args:
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif  len(kwargs) !=0:
            for key, value in kwargs.items():
                setattr(self,key, value)
        else:
            print()

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        square_rep = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return square_rep
