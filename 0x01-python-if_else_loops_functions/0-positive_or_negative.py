#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print ("is zero")
elif number >= 1:
    print ("is positive")
else:
    print ("is negative")
