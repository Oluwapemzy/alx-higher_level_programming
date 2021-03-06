#!/usr/bin/python3
"""Module contains function which appends a string at the end of file"""


def append_write(filename="", text=""):
    """FUnction appends text to end of file
    Args:
    filename - name of file
    text- string to append
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
