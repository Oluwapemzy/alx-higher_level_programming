#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_replaced = []
    for item in my_list:
        if item == search:
            item = replace
        new_replaced.append(item)
    return new_replaced
