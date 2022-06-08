#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_uniq = []
    sum_uniq = 0
    for item in my_list:
        if item not in my_uniq:
            my_uniq.append(item)
    for uniq in my_uniq:
        sum_uniq += uniq
    return(sum_uniq)
