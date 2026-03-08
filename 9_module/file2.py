#module/package/library

# import file1
# print(file1.name)
# print(file1.age)

# file1.sample_function()

# c1=file1.Circle(5)
# print(c1.area())
# print(c1.circumference())   

import asdfkljaslkdjfklajsdflkjasldkfjalskdfjla as p1

print(p1.price)

# from file1 import name,age
from file1 import *
print(name)
print(age)

#inbuild library

import random

print(random.randint(1,100))

import math

print(math.sqrt(16))

import time
print('first')
time.sleep(2)
print('second')

# num=0
# while True:
#     print(num)
#     num=num+1
#     time.sleep(1)

import os
print(os.getcwd())

import sys

num=0
while True:
    if num==5:
        sys.exit()
        # break
    print(num)
    num=num+1
    time.sleep(1)

print('last line')