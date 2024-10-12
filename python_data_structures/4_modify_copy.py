#!/usr/bin/env python3
def el_replace(l, ind, el):
    modified_l = l[:]
    for i in range(len(l)):
        if ind > len(l)-1:
            return f"Index out of range"
        if i == ind:
            modified_l[i] = el
    return f"Copy: {modified_l}\n Original: {l}"



lst1 = [5, 4, 3, 2, 1]
el1 = 5
ind1 = 1

lst2 = [1, 3, 6, 7]
el2 = 0
ind2 = 3

lst3 = [0, 1, 2, 3, 4, 5]
el3 = 10
ind3 = 6

print(el_replace(lst1, ind1, el1))
print(el_replace(lst2, ind2, el2))
print(el_replace(lst3, ind3, el3))
