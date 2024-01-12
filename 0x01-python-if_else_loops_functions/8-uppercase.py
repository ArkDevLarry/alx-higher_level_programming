#!/usr/bin/python3
def uppercase(str):
    cstr = ""
    for char in str:
        if ord("a") <= ord(char) <= ord("z"):
            append = chr((ord(char) - ord("a")) + ord("A"))
        else:
            append = char

        cstr += append

    return cstr
