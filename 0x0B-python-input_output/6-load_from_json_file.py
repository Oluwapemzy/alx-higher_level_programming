#!/usr/bin/python3
"""Module of function creates an object from JSON file"""


def load_from_json_file(filename):
    """Function creates an Object from JsSON file"""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
