#!/usr/bin/python3
""" some comment """


def write_file(filename="", text=""):
    """ some code """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
