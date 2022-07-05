#!/usr/bin/python3
""" Module saves into a file in Json Format"""
import json


def save_to_json_file(my_obj, filename):
    """Function writes to textfile in JSON format"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
