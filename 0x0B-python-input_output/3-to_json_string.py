#!/usr/bin/python3
""" MOdule of function that return Json of object"""
import json


def to_json_string(my_obj):
    """convert to JSON format"""

    return json.dumps(my_obj)
