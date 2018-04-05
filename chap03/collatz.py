#!/bin/python3
# coding: utf-8



def collatz():
    
    while True:
        try:
            print('请输入: ')
            number = int(input())
            
            #肯定是int
            value = (number % 2)

            if value == 0:
                out = (number //2)
            if value == 1:
                out = (number * 3 + 1)
           
            while out != 1:
                    print('请重新输入: ')
                    number = int(input())
                    value = (number % 2)

                    if value == 0:
                        out = (number //2)
                    if value == 1:
                        out = (number * 3 + 1)
            print('结果: ' + str(out))
            break
        except:#ValueError:
            print('输入值必须为整数!')


collatz()
