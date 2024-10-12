#!/usr/bin/python3
def reverse_l(l):
    indx = len(l) - 1
    while indx >= 0:
        print(l[indx])
        indx -= 1

list_ = [5, 4, 3, 2, 1]
reverse_l(list_)


