#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_list in range(len(matrix)):
        x = matrix[sub_list]
        for item in x:
            print("{}".format(item), end=" ")
        print("")
