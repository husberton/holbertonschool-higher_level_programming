#!/usr/bin/python3
""" jhhh """
import json


def class_to_json(obj):
    """ gjgj """
    serialized = dict()
    for attr in dir(obj):
        if attr in [list, dict, str, int, bool]:
            serialized[attr] = obj.attr
    return json.dumps(serialized)
