#!/usr/bin/python3
""" MOdule which contains function thatt writes a string to text file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file
    Args
    filename: name of file
    text: string to write to text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
