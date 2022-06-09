#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    times_num = lambda the_list: the_list * number
    new_list = list(map(times_num, my_list))
    return new_list
