#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    my_max = my_list[0]
    for item in range(len(my_list)):
        if my_list[item] > my_max:
            my_max = my_list[item]
    return my_max
