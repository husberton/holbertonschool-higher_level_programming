#!/usr/bin/python3
def uppercase(str):
    text = ""
    for i in range(len(str)):
        if ord(str[i]) >= ord("a") and ord(str[i]) <= ord("z"):
            print(chr(ord(str[i]) - 32), end="")
        else:
            print(str[i], end="")
    print("")

uppercase("Hello, my name is")
