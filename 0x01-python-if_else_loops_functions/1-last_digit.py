#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10 if number > 0 else int(repr(number)[-1]) * -1
message = "Last digit of "
if (last_digit > 5):
    print("{}{} is {} and is greater than 5".format(message, number, last_digit))
elif (last_digit == 0):
    print("{}{} is {} and is 0".format(message, number, last_digit))
else:
    print("{}{} is {} and is less than 6 and not 0".format(message, number, last_digit))
