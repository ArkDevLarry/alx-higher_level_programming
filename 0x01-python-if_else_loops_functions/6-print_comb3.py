#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(0, 10):
        if str(num1) + str(num2) == "89":
            print("{}{}".format(num1, num2))
        elif not (num1 >= num2):
            print("{}{}".format(num1, num2), end=", ")
