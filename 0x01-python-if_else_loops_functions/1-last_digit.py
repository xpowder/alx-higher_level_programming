#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
last_digit_negative = -last_digit if number < 0 else last_digit

print(f"Last digit of {number} is {last_digit_negative} and is", end=" ")

if last_digit_negative > 5:
    print("greater than 5")
elif last_digit_negative == 0:
    print("0")
else:
    print("less than 6 and not 0")
