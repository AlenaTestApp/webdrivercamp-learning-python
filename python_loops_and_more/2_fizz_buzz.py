#!/usr/bin/env python3
def fizz_buzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
        print(i, end = ' ')

fizz_buzz(100)
