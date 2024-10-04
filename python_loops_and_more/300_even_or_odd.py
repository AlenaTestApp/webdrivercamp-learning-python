#!/usr/bin/python3
import random
random_num = random.randint(-10000, 10000)
last_char = int(str(random_num)[-1])
if last_char == 0:
    print(f'{random_num} - the last digit {last_char}  is zero')
elif last_char%2 == 1:
    print(f'{random_num} - the last digit {last_char}  is odd')
else:
    print(f'{random_num} - the last digit {last_char}  is even')
