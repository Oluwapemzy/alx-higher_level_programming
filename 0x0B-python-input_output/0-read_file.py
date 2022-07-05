#!/usr/bin/python3
"""Module of a function that reads from a file"""


def read_file(filename=""):
    """Function that reads from a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        my_data = f.read()
        print(my_data, end='')
