#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 2:
        print("{} argument:".format(len(args) - 1))
    else:
        print("{} arguments".format(len(args) - 1), end='')
        if len(args) == 1:
            print(".")
        else:
            print(":")
    for i in range(1, len(args)):
        print("{:d}: {}".format(i, args[i]))
