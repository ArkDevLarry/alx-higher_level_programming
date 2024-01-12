#!/usr/bin/python3
for num in range(0, 100):
    if num > 9:
        print(f"{}".format(num), end=", ")
    else:
        print(f"0{}".format(num), end=", ")
