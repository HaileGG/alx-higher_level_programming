#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = " and is greater than 5"
str2 = " and is 0"
str3 = " and is less than 6 and not 0"
if number < 0:
    nb = number % -10
else:
    nb = number % 10
if nb > 5:
    print("Last digit of {} is {}".format(number, nb) + str1)
elif nb == 0:
    print("Last digit of {} is {}".format(number, nb) + str2)
else:
    print("Last digit of {} is {}".format(number, nb) + str3)
