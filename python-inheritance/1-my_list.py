#!/usr/bin/python3
""" Create a class """


class MyList(list):
    """ This class customizes list """
    def print_sorted(self):
        print(sorted(self))
