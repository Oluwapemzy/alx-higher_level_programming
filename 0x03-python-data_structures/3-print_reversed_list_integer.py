#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for item in range(len(my_list)):
        print("{:d}".format(my_list[len(my_list) - item - 1]))
