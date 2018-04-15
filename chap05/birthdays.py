#!/bin/python3
# coding: utf-8


#dic

birthdays = {'A': 'Apr 1', 'B': 'Dec 12', 'C': 'Mar 4'}

while True:
    print('请输入姓名： (空表示退出)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' 是 ' + name + '的生日')
    else:
        print('我不知道 ' + name + '的生日')
        print('生日是何时？')
        bday = input()
        birthdays[name] = bday
        print('生日已记录！')
