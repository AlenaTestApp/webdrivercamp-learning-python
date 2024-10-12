#!/usr/bin/env python3
def tuple_addition(first_arg, second_arg):
    first_1 = first_arg[0] if len(first_arg) > 0 else 0
    first_2 = first_arg[1] if len(first_arg) > 1 else 0
    second_1 = second_arg[0] if len(second_arg) > 0 else 0
    second_2 = first_arg[0] if len(first_arg) > 0 else 0
    return first_1 + second_1, first_2 + second_2


print(tuple_addition((1, 99), (-1, 1)))
print(tuple_addition((1,), (1, )))
print(tuple_addition((1, 2, 3, 4), (-1, -2, -3, -4)))
print(tuple_addition((), (1,)))
print(tuple_addition((1, 99), (-1, 1)))
print(tuple_addition((),()))
