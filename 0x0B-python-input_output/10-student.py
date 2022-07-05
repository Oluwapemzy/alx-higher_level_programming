#!/usr/bin/python3
"""Class student"""


class Student:
    """Contains student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict of student"""

        if attrs == None or type(attrs) != list:
            return self.__dict__
        else:
            sto = {}
            for item in attrs:
                if type(item) != str:
                    return self.__dict__
                if item in self.__dict__.keys():
                    sto[item] = self.__dict__[item]
            return sto
