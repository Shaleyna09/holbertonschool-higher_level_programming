#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = new_element
    return my_list
