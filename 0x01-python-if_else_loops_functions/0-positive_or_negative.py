#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
last_digit = number%10
#set sign for last digit
if number < 0:
    last_digit = last_digit*(-1)
print statements 
if last_digit>5:
    print("Last digit of {number:d} is {last_digit:d} and is greater than 5")
elseif last_digit!=0 and last_digit<6:
    print("Last digit of {number:d} is {last_digit:d} and is less than 6 and not 0")
else:
    print("Last digit of {number:d} is {last_digit:d} is 0")
