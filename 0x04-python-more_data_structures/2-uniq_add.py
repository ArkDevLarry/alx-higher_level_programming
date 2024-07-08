#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer).
    """
    nlist = []
    sum = 0
    for n in my_list:
        if n not in nlist:
            sum += n
            nlist.append(n)
    return sum
