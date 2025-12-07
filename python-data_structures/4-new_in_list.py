#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list[:]
    if not (idx < 0 or idx > len(list)) - 1:
        list[idx] = element
    return list
