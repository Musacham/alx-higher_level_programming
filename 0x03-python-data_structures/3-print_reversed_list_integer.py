#!/usr/bin/python3
def print_reverse_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in reversed(my_list):
        print('{:d}'.format(i))
