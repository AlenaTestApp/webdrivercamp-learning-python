#!/usr/bin/env python3
def eval_list(l):
    tup = ()
    for el in l:
        if el%2 == 0:
            tup += (True,)
        else:
            tup += (False,)
    return tup


my_list = [5, 4, 3, 2, 1]
print(eval_list(my_list))

