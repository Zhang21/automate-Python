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



## 用正则表达式匹配更多模式


<br>


### 利用括号分组


添加括号`()`将在正则表达式中创建**分组**，如将区号从电话号码中分离: `(\d\d\d)-(\d\d\d-\d\d\d\d)`；然后使用`group()`匹配对象。
如果想要一次就获取所有分组，请使用`groups()`方法，返回多个值的元祖。

```py
import re
mo = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)').search('My number is 123-456-7890.')


mo.group()
#'123-456-7890'
mo.group(0)
#'123-456-7890'

mo.group(1)
#'123'

mo.group(2)
#'456-7890'

mo.groups()
#('123', '456-7890')

```


<br>


### 用管道匹配多个分组


管道符 `|`，匹配多个表达式中的一个。如：`r'AAA|BBB'`

通过使用管道字符和分组括号，可以指定集中可选的模式，让正则表达式去匹配。

```py
import re
mo1 = re.compile(r'AAA|BBB').search('AAA or BBB.')
mo2 = re.compile(r'AAA|BBB').search('BBB or AAA.')


mo1.group()
#'AAA'

mo2.group()
#'BBB'


mo3 = re.compile(r'zhang(21|22|23)').search('zhang21 is a nickname.')


mo3.group()
#'zhang21'

mo3.group(1)
#'21'
```

<br>


### 用问号实现可选匹配


字符`?`表明它面前的分组在这个模式中是可选的。

```py
import re

mo1 = re.compile(r'AAA(zhang)?BBB').search('is AAABBB word.')
#(zhang)?是可选部分


mo1.group()
#'AAABBB'

mo2 = re.compile(r'AAA(zhang)?BBB').search('is AAAzhangBBB word.')

mo2.group()
#'AAAzhangBBB'

```


<br>


### 用星号匹配零次或多次


星号`*`匹配零次或多次`>=0`。

```py
import re

mo1 = re.compile(r'AAA(or)*BBB').search('is AAABBB word.')
mo2 = re.compile(r'AAA(or)*BBB').search('is AAAorBBB word.')
mo3 = re.compile(r'AAA(or)*BBB').search('is AAAorororBBB word.')

mo1.group()
#'AAABBB'

mo2.group()
#'AAAorBBB'

mo3.group()
#'AAAorororBBB'
```


<br>


### 用加号匹配一次或多次


加号`+`匹配一次或多次`>=1`。

```py
import re

mo1 = re.compile(r'AAA(and)+BBB').search('is AAABBB word.')
mo2 = re.compile(r'AAA(and)+BBB').search('is AAAandBBB word.')
mo3 = re.compile(r'AAA(and)+BBB').search('is AAAandandandBBB word.')

mo1.group()
#报错，无匹配对象

mo2.group()
#'AAAandBBB'

mo3.group()
#'AAAandandandBBB'

```


<br>


### 用花括号匹配特定次数


花括号`{}`匹配特定的次数，可以是数字或范围。

```py
import re

mo1 = re.compile(r'(Ha){3}').search('HaHaHa')
mo2 = re.compile(r'(Ha){3,5}').search('HaHaHaHa')

mo1.group()
#'HaHaHa'

mo2.group()
#'HaHaHaHa'
```


<br>
<br/>


## 贪婪匹配和非贪婪匹配


Python的正则表达式默认是**贪婪**的，它会尽可能匹配最长的字符串。而非贪婪则匹配最短的字符串。

请注意，问号在正则表达式中可能有两种含义：

- 声明非贪婪匹配
- 表示可选的分组

```py
import re

greedyRe = re.compile(r'(Ha){3,5}')
nonGreedRe = re.compile(r'(Ha){3,5}?')

mo1 = greedyRe.search('HaHaHaHaHa')
mo2 = nonGreedRe.search('HaHaHaHaHa')

mo1.group()
#'HaHaHaHaHa'

mo2.group()
#'HaHaHa'
```


<br>


## findall()方法


- `search()`返回一个匹配的对象，包含被查找字符串中欧冠的第一次匹配的文本
- `findall()`返回一组字符串列表，包含被查找字符串中的所有匹配

```py
import re

reg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = reg.search('Home: 111-222-3333 Office: 123-456-7890')
mo.group()
#'111-222-3333'

reg.findall('Home: 111-222-3333 Office: 123-456-7890')
#['111-222-3333', '123-456-7890']

```


<br>


## 字符分类


有很多缩写的字符分类：

| 缩写 | 描述 |
| - | - |
| \d | 0-9的任一数字 |
| \D | 除0-9的数字外的任何字符 |
| \w | 任何字母、数字和下划线字符(可以认为是匹配单词字符) |
| \W | 除字母、数字和下划线以外的任何字符 |
| \s | 空格、制表符和换行符 |
| \S | 除空格、制表符和换行符以外的任何字符 |

```py
import re

reg = re.compile(r'\d+\s\w+')
reg.findall('12 abc, 11 dcd, 10 cde, 9 defg')
#['12 abc', '11 dcd', '10 cde', '9 defg']

```


<br>


## 建立自己的字符分类


如字符分类[aeiouAEIOU]将匹配所有的元音字符，不论大小写。

```py
import re

reg = re.compile(r'[aeiouAEIOU]')

reg.findall('RoboCop eats baba food. Food.')
#['o', 'o', 'o', 'e', 'a', 'a', 'a', 'o', 'o', 'o', 'o']


#匹配非元音字符
reg2 = re.compile(r'[^aeiouAEIOU]')
reg2.findall('RoboCop eats baba food. Food.')

#['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', ' ', 'f', 'd', '.', ' ', 'F', 'd', '.']

```


<br>
<br/>


## 插入字符和美元字符


- 在正则表达式的开始出使用插入符号`^`，表明匹配必须发生在被查找的文本开始处
- 在正则表达式末尾加上美元符号`$`，表示该字符串必须以这个正则表达式的模式结束
- 同时使用`^`和`$`，表示真个字符串必须匹配该模式

```py
import re

reg = re.compile(r'^\d+END$')

reg.search('12345END')

```

<br>
<br/>


## 通配符


在正则表达式中，句点`.`字符被称为**通配符**。它匹配除了换行之外的所有字符。

```py
import re

reg = re.compile(r'.at')
reg.findall('the cat in the hat sat on the flati 3at.')
#['cat', 'hat', 'sat', 'lat', '3at']

```


<br>


### 用点-星匹配所有字符


```py
import re

reg = re.compile(r'1st name: (.*) 2nd name: (.*)')
mo = reg.search('1st name: Zhang 2nd name: xxx')

mo..group(1)
#'zhang'
```


<br>


### 用句点字符匹配换行


将`re.DOTALL`作为`re.compile()`的第二个参数，可以让句点字符匹配所有字符，包括换行字符。

```py
import re

reg = re.compile('.*')
reg.search('line01.\nline02\nline03').group()
#'line01.'


reg2 = re.compile('.*', re.DOTALL)
reg2.search('line01.\nline02\nline03.').group()
#'line01.\nline02\nline03.'

```


<br>
<br/>


## 不区分大小写的匹配

通常，正则表达式用你制定的大小写来匹配文本。你可以向`re.compile()`传入`re.IGNORECASE`或`re.I`作为第二个参数，以忽略大小写。

```py
import re

reg = re.compile(r'aBc', re.I)

reg.findall('it is ABC or abc.')
#['ABC', 'abc']

```


<br>
<br/>


## 替换字符串


正则表达式不仅能找到文本模式，而且能够用新的文本替换掉这些模式。

Regex对象的`sub()`方法需要传入两个参数。第一个参数用于取代发现的匹配；第二个参数是正则表达式。

```py
import re

reg = re.compile(r'zhang \d+')
reg.sub('SUBsub', 'zhang 1234 zhang ABCD.')
#'ZHANG zhang ABC123.'

```


<br>

---

<br/>


## 管理复杂的正则表达式


如果要匹配的文本模式很简单，正则表达式就很好写。但匹配复杂的文本模式，可能需要很长、很费解的正则表达式。

可以向`re.compile()`传入变量`re.VERBOSE`作为第二个参数，以忽略正则表达式串中的空白符和注释。

```py
import re

reg = re.compile(r'((\d{3}|\(\d{3}\)?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')


#加上注释的正则表达式
reg = re.compile(r'''(
    (\d{3}|\(\d{3}\))?		#area code
    (\s|-|\.)?			#separator
    \d{3}			#3 digits
    (\s|-|\.)			#separator
    \d{4}			#4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? #extension
)''', re.VERBOSE)

```


<br>

---

<br/>


## 组合使用re.IGNORECASE、re.DOTAIL、re.VERBOSE


`re.compile()`函数只接受一个值作为它的第二个参数。但可以使用管道符`|`将变量组合起来，从而绕过这个限制。

```py
import re

reg = re.compile('foo', re.IGNORECASE | re.DOTAIL | re.VERBOSE)

```


<br>

---

<br/>


## 提取电话号码和E-mail的小程序


见`find_NE.py`



<br>

---

<br/>


## 实践项目


- 强口令检测
	+ `strong_Passwd.py`
- `strip()`的正则表达式


























































