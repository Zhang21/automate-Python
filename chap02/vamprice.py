#!/bin/python3
# coding: utf-8

print('input name: ')
name = str(input())
print('input age: ')
age = int(input())

if name == 'a':
    print('a')
elif age < 12:
    print('lt 12')
elif age > 100:
    print('gt 100')
else:
    print('other!')



