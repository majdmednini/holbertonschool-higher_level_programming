#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = len(sys.argv) - 1
    if index == 0:
        print("0 arguments.")
    elif index == 1:
        print("1 argument:")
    else:
        print(index + "arguments:")
    for i in range(index):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
