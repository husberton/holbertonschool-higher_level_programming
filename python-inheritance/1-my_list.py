#!/usr/bin/python3
""" Create a class """


class MyList(list):
    """ This class customizes list """
    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print(new_list)
