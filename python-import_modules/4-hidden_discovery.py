#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    files = [file for file in dir(hidden_4) if not file.startswith("__")]
    for file in files:
        print(file)
