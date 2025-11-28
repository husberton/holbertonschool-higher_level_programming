#!/usr/bin/python3
def remove_char_at(str, n):
    text = ""
    for i in range(len(str)):
        if i == n:
            continue
        text += str[i]
    return text
