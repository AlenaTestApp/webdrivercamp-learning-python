#!/usr/bin/env python3
def tuple_return(lst):
    return (0, None) if len(lst) == 0 else (len(lst), lst[0])



l = [1, 2, 3, 4, 5]
list_len, first_element = tuple_return(l)
print(f"List len = {list_len}\nFirst element = {first_element}")
l = []
list_len, first_element = tuple_return(l)
print(f"List len = {list_len}\nFirst element = {first_element}")
