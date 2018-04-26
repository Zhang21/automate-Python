#!/bin/python3
# coding: utf-8


#finds phonenumbers and E-mails from the clipboard.

import pyperclip, re


phone_Reg = re.compile(r'''
  (
    (\d{3}||(|d{3}\))?		#区号
    (\s|-|\.)?			#分隔符
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5))?
  )''', re.VERBOSE
)


email_Reg = re.compile(r'''
  (
    [a-zA-Z0-9._%+-]+	#用户名
    @
    [a-zA-Z0-9._]	#域名
    (\.[a-zA-Z]{2,4})
  )''', re.VERBOSE
)


#剪贴板
text = str(pyperclip.paste())
matches = []
for groups in phone_Reg.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)


for groups in email_Reg.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')
