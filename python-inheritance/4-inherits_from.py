#!/usr/bin/python3
""" a function """


def inherits_from(obj, a_class):
    """ issubclass """
    return issubclass(type(obj), a_class) and obj is not a_class
