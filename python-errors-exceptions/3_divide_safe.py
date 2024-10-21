#!/usr/bin/env python3
def divide_safe(a, b):
    res = 0
    try:
        res = a/b
    except ZeroDivisionError as e:
        print(f"ERROR OCCURRED: {e}")
        res = None

    finally:
        return res

if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"RESULT: {result}")
    print(f"{a} / {b} = {result}")
    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
    print(f"RESULT: {result}")
