#!/usr/bin/env python3
def calc_weight(list_=[]):
    total_score = 0
    total_weght = 0
    for i in list_:
        score = i[0]
        weight = i[1]
        total_score += score * weight
        total_weght += weight
    if total_weght > 0:
        res = total_score / total_weght
    else:
        res = 0
    return res

list_ = [(3, 2), (5, 9), (7, 7)]
result = calc_weight(list_)
print(f"Weight: {result:0.2f}")
print("===============================")
list_1 = [(3, 0), (5, 0), (7, 0)]
result = calc_weight(list_1)
print(f"Weight: {result:0.2f}")
print("===============================")
