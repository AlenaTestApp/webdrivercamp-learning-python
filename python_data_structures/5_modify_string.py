#!/usr/bin/env python3
string1 = '"""AbraCadabra'
string2 = 'A new string voila!"""'

def modify(string, char):
    res = ''
    for c in string:
        if c.lower() != char.lower() or c.upper() != char.upper():
            res += c
    return res

print(modify(string1, "a"))
print(modify(string2, "A"))
