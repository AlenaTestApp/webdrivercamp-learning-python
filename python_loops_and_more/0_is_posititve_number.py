#!/usr/bin/python3
import random
random_num = random.randint(-10, 10)
print("Evaluate number")
number = random_num

if number > 0:
	status = "positive"
elif number < 0:
	status = "negative"
else:
	status = "zero"
print(f'{number} is  {status}') 
