#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sub_list in matrix:
        squ_list = list(map((lambda x: x ** 2), sub_list))
        new_matrix.append(squ_list)
    return new_matrix
