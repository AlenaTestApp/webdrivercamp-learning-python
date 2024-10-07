#!/usr/bin/env python3
def is_case(c):
    if ord(c) in range(ord('a'), ord('z') + 1):
        return True
    else:
        return False

print(is_case("A"))
print(is_case("c"))
print(is_case("M"))
print(is_case("i"))
