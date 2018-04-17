#!/bin/python3
# coding: utf-8

import sys, pyperclip

pwd = {'qq': '@qq.com',
    'email1': '@email.com',
    'wechat': '@wechat.com'
}

if len(sys.argv) < 2:
    print('用法： python3 pw.py [username]')
    sys.exit()

#0表示pw.py
username = sys.argv[1]

if username in pwd:
    pyperclip.copy(pwd[username])
    print('用户' + username + ' 的密码已复制')
else:
    print('用户不存在')
 
