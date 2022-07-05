#!/usr/bin/python3
"""Module Creates a class"""


class Student:
    """Class creates new instances of Student"""

    def __init__(self, first_name, last_name, age):
        """init function of Class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns class dict description"""
        return self.__dict__
