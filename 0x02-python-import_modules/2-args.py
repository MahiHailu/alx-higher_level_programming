#!/usr/bin/python3
if __name__ == "__main__":
    """Print the num of and list of argu"""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 argu.")
    elif count == 1:
        print("1 argu:")
    else:
        print("{} argu:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
