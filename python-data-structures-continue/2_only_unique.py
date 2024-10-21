#!/usr/bin/env python3
def only_unique(list_=[]):
    unique_list = []
    total = 0
    for i in list_:
        if i not in unique_list:
            unique_list.append(i)
            total += i
    return total        



if __name__=="__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")


