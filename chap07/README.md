# 模式匹配与正则表达式


- 不用正则表达式来查找文件模式
- 使用正则表达式来查找文本模式
    + 创建正则表达式对象
    + 匹配Regex对象
    + 正则表达式匹配复习
- 用正则表达式匹配更多模式
    + 利用括号分组
    + 用管道匹配多个分组
    + 用问号实现可选匹配
    + 用星号匹配零次或多次
    + 用加号匹配一次或多次
    + 用花括号匹配特定次数
- 贪婪和非贪婪匹配
- findall()方法
- 字符分类
- 建立自己的字符分类
- 插入字符和美元字符
- 通配字符
    + 用点-星匹配所有字符
    + 用句点字符匹配换行
- 正则表达式符号复习
- 不区分大小写的正则匹配
- 用sub()方法替换字符串
- 管理复杂的正则表达式
- 组合使用re.IGNORECASE, re.DOTALL, re.VERBOSE


<br>

---

<br/>


## 不用正则表达式来查找文本模式


假设我们要在文本中匹配一个电话号码，格式像这样`123-456-7890`.

```py

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print('123-456-7890 is a phone number: ' )
print(isPhoneNumber('123-456-7890'))

print('Moshi moshi is a phone number: ')
print(isPhoneNumber('Moshi moshi'))



message = 'call me at 123-321-4444 tomorroe . 111-222-3333 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('phone number found: ' + chunk)

print('Done!')

```


<br>

---

<br/>


## 用正则表达式查找文本模式


正则表达式，简称regex, re，是文本模式的描述方法


<br>


### 创建正则表达式对象


Python中所有正则表达式的函数都在re模块中。
向`re.compile()`传入一个字符串值，表示正则表达式，它将返回一个Regex模式对象，简称`Regex对象`。


```py

import re

#如前面的电话号码
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

```

<br>


### 匹配Regex对象


`Regex对象`的`search()`方法查找传入的字符串，寻找该正则表达式的所有匹配。

- 如果字符串没有找到该正则表达式模式，`search()`方法将返回`None`
- 如果找到了该模式，`search()`方法将返回一个Match对象


```py
import re

mo = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d').search('My number is 123-456-7890.')
print('Phone number found: ' + mo.group())

#Phone number found: 123-456-7890

```


<br>


### 正则表达式复习

在Python中使用正则表达式的大概步骤：

1. 使用`import re`导入模块
2. 用`re.compile()`函数创建一个Regex对象
3. 向Regex对象的`search()`方法传入向查找的字符串
4. 调用Match对象的`group()`方法，放回实际匹配的字符串


<br>

---

<br/>






















