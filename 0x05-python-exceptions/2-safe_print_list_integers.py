#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    no_of_int = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            no_of_int += 1
        except TypeError:
            pass
        except ValueError:
            pass

    print("")
    return no_of_int
