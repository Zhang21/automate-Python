# 字符串操作


- 处理字符串
    + 字符串字面量
    + 双引号
    + 转义字符
    + 原始字符串
    + 用三重引号的多行字符串
    + 多行注释
    + 字符串下标和切片
    + 字符串的in和not in
- 有用的字符串方法
    + upper(), lower(), isupper(), islower()
    + isX
    + startswith(), endswith()
    + join(), split()
    + 用rjust(), ljust(), center()对齐文本
    + 用strip(), rstrip(), lstrip()删除空白字符
    + 用pyperclip模块拷贝粘贴字符串



<br>
<br/>

---

<br>



## 处理字符串


文本是程序需要处理的最常见的数据形式。
Python提供了写入、打印和访问字符串的一些方法。

<br>


- 字符串以**单引号**/**双引号**开始和结束

- 单双引号是为了在文本中能使用单双引号

- 也可以使用转移字符(`\`)对单双引号进行转义
    + `\'`, `\'`, `\t`, `\n`, `\\`

- 可在字符串引号前加上`r`，使它成为**原始字符串**
    + 原始字符串完全忽略所有的转义字符

```
print(r'It is ABC\'s cat.')

It is ABC\'s cat.

```

- 用三重引号表示多行字符串

```
print(''' Line 1,
Line 2,

Line 3,
Line 4''')


```

- 多行注释

```
"""It is comments
xxx

end of comments.
"""

```

- 字符串像列表一样，可以使用下标和切片

```
string = 'Hello'

print(string[0])
print(string[-1]
print(string[1:])

```

- 字符串也能使用`in`和`not in`操作符

```
'hello' in 'hello world'

True

```


<br>
<br/>

---

<br/>



## 字符串方法


- `upper()`
    + 将字符串转换为小写
- `lower()`
    + 将字符串转换为大写
- `isupper()`
    + 判定所有字符都为小写
- `islower()`
    + 判定所有字符都为大写

- `isX`
-  `isalpha()`
    + 判定字符串只包含非空字母
-  `isalnum()`
    + 判定字符串只包含非空字母数据
-  `isdecimal()`
    + 判定字符串只包含非空数字
-  `isspace()`
    + 判定字符串只包含空格、制表符和换行
-  `istitle`
    + 判定字符串只包含以大写字母开头、后面都是小写字母

- `startwith()`
    + 判定字符串的开始字符
- `endswith()`
    + 判定字符串的结束字符

- `join()`
    + 将一个字符串列表连接成一个单独的字符串
- `split()`
    + 针对一个字符串返回一个字符串列表

 ```py
'-'.join(['a', 'b', 'c'])
'a-b-c'

'hello world'.split()
[hello', 'world']

'a-b-c'.split('-')
['a', 'b', 'c']

 ```

- `rjust()`
    + 右对齐
- `ljust()`
    + 左对齐
- `center()`
    + 居中

```py
'hello'.rjust(10)
'     hello'

'hello',ljust(10, '-')
'hello-----'

'hello'.center(11)
'   hello   '

'hello'.center(11, '-')
'---hello---'
```

- `strip()`
    + 删除两边字符
- `rstrip()`
    + 删除右边字符
- `lstrip()`
    + 删除左边字符

```py
'  hello'.lstrip()
'hello'

'abchelloabc'.strip('abc')
'hello'

```

- `pyperclip模块`
- `pyperclip.copy()`
    + 向计算机的剪贴板发送文本
- `pyperclip.paste()`
    + 从剪贴板接受文本

```py
#pip3 install pyperclip

import pyperclip


pyperclip.copy('hello')
pyperclip.paste()
'hello'

```






























