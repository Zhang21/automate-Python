#!/bin/python3
# coding: utf-8


nameList = []

while True:
    print('请输入名字：')
    name = input()
    if name == '':
        break
    nameList = nameList + [name]
print('名单如下：')
for name in nameList:
    print(name)
