#!/usr/bin/python3
'''append write fnc'''


def append_write(filename="", text=""):
    '''function that appends a string at the end of a text file'''
    with open(filename, 'a') as file:
        file.write(text)
    return len(text)
