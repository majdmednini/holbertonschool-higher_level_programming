#!/usr/bin/python3
""" Module Square """


class Square:
    """ Square Class """
    def __init__(self, size=0):
        """ The size of square """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
                raise TypeError('size must be an integer')
