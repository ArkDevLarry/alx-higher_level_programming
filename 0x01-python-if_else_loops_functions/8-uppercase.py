#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for char in str:
        if ord("a") <= ord(char) <= ord("z"):
            c = chr((ord(char) - ord("a")) + ord("A"))
        print("{}", format(c))

    return cstr
