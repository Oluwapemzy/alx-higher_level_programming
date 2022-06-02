#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    sums = 0
    for num in range(1, len(argv)):
        sums += int(argv[num])
    print(sums)
