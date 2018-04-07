#!/bin/python3
# docing: utf-8


#import random
from random import randint

messages = [ 'aaaaa', \
            'bbbbb', \
            'ccccc', \
            'ddddd', \
            'eeeee', \
            'fffff' ]

print(messages[randint(0, len(messages) - 1)])

