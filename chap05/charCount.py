#!/bin/python3
# coding: utf-8


import pprint

message = 'Liverpool are the champios, YNWA!'

count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)
#print(pprint.pformat(count))
