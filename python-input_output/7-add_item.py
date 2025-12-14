#!/usr/bin/python3
""" some code """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]

save_to_json_file(arguments, "add_item.json")
with open("add_item.json", 'a', encoding='utf-8') as f:
    f.write("\n")
