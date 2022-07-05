#!/usr/bin/python3
"""Module of function return an object in JSOn"""


def from_json_string(my_str):
    """Function that returns an object by a JSON representation"""
    return json.loads(my_str)
