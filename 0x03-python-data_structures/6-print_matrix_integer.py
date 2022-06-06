#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_list in range(len(matrix)):
        x = matrix[sub_list]
        for item in range(len(x)):
            print("{:d}".format(x[item]),
                  end=" " if item < len(matrix[sub_list]) - 1 else "")
        print("")
