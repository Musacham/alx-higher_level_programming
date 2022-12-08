#!/usr/bin/python3
def sorted_dictionary(my_dict):
    for keys in sorted(my_dict.keys()):
        print('{}: {}'.format(keys, my_dict[keys]))
