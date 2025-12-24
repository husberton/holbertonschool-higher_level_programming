#!/usr/bin/python3
import json
""" Python serialization """


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)
    return "The data has been serialized and saved to 'data.json'"

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data