#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    ele_1 = tuple_a[0] + tuple_b[0]
    ele_2 = tuple_a[1] + tuple_b[1]
    new_tuple = (ele_1, ele_2)
    return new_tuple
