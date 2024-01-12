#!/usr/bin/python3
for num in range(0, 100):
    if num > 9:
        print("{}".format(num), end=", ")
    else:
        print("0{}".format(num), end=", ")
