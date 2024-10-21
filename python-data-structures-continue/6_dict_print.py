#!/usr/bin/python3
def dict_print(dict_):
    for key in sorted(dict_):
        print(key, dict_[key])

dct = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
dict_print(dct)

