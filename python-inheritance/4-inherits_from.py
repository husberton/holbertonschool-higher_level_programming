#!/usr/bin/python3
""" a function """


def inherits_from(obj, a_class):
    """ issubclass """
    return issubclass(type(obj), a_class) and obj.__name__ is a_class
