#!/bin/bash
#coding: utf-8



#强口令：长度不少于8个字符，同时包含大小写，至少一位数字。


import re



def strong():
    print('请输入密码： ')
    passwd = str(input())
    
    if len(passwd) < 8:
        print('Weak passwd!')
    else:
        if re.compile(r'\d+').search(passwd) == None:
            print('NO digit!')
        else:
            if re.compile(r'[a-z]+').search(passwd) == None:
                print('No lowercase!')
            else:
                if  re.compile(r'[A-Z]+').search(passwd) == None:
                    print('NO uppercase!')
                else:
                    print('Strong passwd!')


strong()








