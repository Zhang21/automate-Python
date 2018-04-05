# 控制流

- 布尔值
- 比较操作符
- 布尔操作符
	+ 二元布尔操作符
	+ not操作符
- 混合布尔和比较操作符
- 控制流的元素
	+ 条件
	+ 代码块
- 程序执行
- 控制流语句
	+ `if`
	+ `else`
	+ `elif`
	+ `while`
	+ `break`
	+ `continue`
	+ `for`
	+ `range()`函数
	+ 等价的`while`循环
- 导入函数
	+ `from import`
- 用`sys.exit()`提前结束程序

> 程序就是一系列指令。
> 控制流语句可以决定在什么条件下执行哪些Python语句。


<br>

---

<br/>


## 布尔值

布尔(Boolean)数据类型只有两种值：

- True
- False


<br>

---

<br/>


## 比较操作符

| 操作符 | 含义
| :- | :-
| == | 等于
| != | 不等于
| < | 小于
| > | 大于
| <= | 小于等于
| >= | 大于等于

操作符根据提供的值，返回True或False。

| 栗子 | 返回值
| - | -
| 42 == 42.0 | True
| 1 == 2 | False
| 2 != 3 | True
| 5 < 7 | True
| 'aa' == 'AA' | False


<br>

---

<br/>


## 布尔操作符

3个布尔操作符用于比较布尔值：

- 与(and),优先级次之
- 或(or)，优先级最低
- 非(not)，优先级最高

<br>

### 二元布尔操作符

`and`和`or`操作符总是接受两个布尔值，所以它们被称为二元操作符。

| 栗子 | 返回值
| - | -
| True `and` False | False
| True `or` False | True

<br>

### not操作符

| 栗子 | 返回值
| - | -
| `not` True | False
| `not` False | True
| `not` `not` True | True


<br>

---

<br/>


## 控制流

控制流语句的开始部分通常是条件(condition)，接下来是一个代码块——称为字句。

```py
name = input()
passwd = input()
if name == 'A':
	print('A')
if passwd == 'BB':
	print('BB')
else:
	print('Other!')
```

<br>

---

<br/>


## 控制流语句

**请避免陷入死循环！**
**在用于条件时，0、0.0和''(空字符)被认为是False，其它值被认为是True。**

```py
#if语句
if name == 'zhang':
	print('Hi, zhang')


#else语句
if name == 'zhang':
        print('Hi, zhang')
else:
	print('Hi, stranger')


#elif语句
if name == 'zhang':
        print('Hi, zhang')
elif age < 12:
	print('ccc')


#while语句，不定循环
count = 5
while count > 0:
    print('Hello')
    count--


#注意死循环


#break语句，跳出循环
while True:
    print('input name')
    name = input()
    if name == 'zhang':
	break
print('tks')


#continue语句，跳到循环开始处
while True:
    print('who are you?')
    name = input()
    if name != 'zhang':
	continue
    print('Hello, zhang,input passwd.')
    passwd = input()
    if passwd == 'zhang21':
	break
print('you are zhang.')


#for循环，固定循环
#range()函数
print('my name is ')
for i in range(5):
    print('times: '+ str(i))
#用while
print('my name is ')
i = 0
while i < 5:
    print('times: ' + str(i))
    i++


#range()的开始、停止和步长
for i in range(0, 10, 2):
    print(i)
for i in range(5, -1, -2):
    print(i)
```

<br>

---

<br/>


## 导入模块

Python程序可以调用一组基本的函数，这称为内建函数。
Python也包括一组模块，称为**标准库**。每个模块都是一个Python程序，包含一组相关的函数，可以嵌入你的程序当中。

```py
#import语句
import random
for i in range(5):
    print(random.randint(1, 10))

import random, sys, os, math


#from import语句
from random import *
for i in range(5):
    print(randint(1, 10))

#不需要带random前缀
#不建议这样使用
#使用完整的名称会让代码更可读

```

<br>

---

<br/>


## 用sys.exit()提前结束程序

当程序执行到指令底部时，总是会终止的。但是，通过`sys.exit()`函数，可让程序终止。






















