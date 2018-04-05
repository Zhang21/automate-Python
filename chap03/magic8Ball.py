#!/bin/python3
# coding: utf-8


import random


def getAnswer(number):
    if number == 1:
        return '1'
    elif number == 2:
        return '22'
    elif number == 3:
        return 'Yes'
    elif number == 4:
        return '4444'
    elif number == 5:
        return '55555'
    else:
        return 'number gt 5'

#r = random.randint(1, 9)
#fortune = getAnswer(r)
#print(fortune)

#将以上三行缩写为
print(getAnswer(random.randint(1, 9)))


