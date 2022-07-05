#!/usr/bin/python3
"""Adds all arguments to a list and save to file"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file


    try:
        my_add = load_from_json_file("add_item.json")
    except FIleNotFoundError:
        my_add = []
    my_add.extend(sys.argv[1:])
    save_to_json_file(my_add, "add_item.json")
