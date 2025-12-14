#!/usr/bin/python3
""" some code """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]

with open("add_item.json", "w", encoding="utf-8") as f:
    save_to_json_file(arguments, f)
