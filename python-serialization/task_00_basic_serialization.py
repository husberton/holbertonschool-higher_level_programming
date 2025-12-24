#!/usr/bin/python3
import pickle
""" Python serialization """


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, "rb") as file:
        return pickle.load(file)