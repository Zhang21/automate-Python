# 函数

- def语句和参数
- 返回值和return语句
- None值
- 关键字参数
- 局部和全局作用域
    + 局部变量不能在全局作用域内使用
    + 局部作用域不能使用其它局部作用域内的变量
    + 全局变量可以在局部作用域中读取
    + 名称相同的局部变量和全局变量
- global语句
- 异常处理

<br>

Python提供了如`print()`、`input()`这样一些内建(built-in)函数，但你也可以编写自己的函数。
函数的一个主要目的就是将需要多次执行的代码放在一起，如果没有函数定义，你可能每次都需要复制粘贴这些代码。
随着你获得更多的编程经验，常常会发现自己在为代码**消除重复**。消除重复能够使程序更短、更易读、更容易更新。


<br>

---

<br/>


## def语句和变量

```py

#!/bin/python3
# coding: utf-8


#自定义参数
def hello(name):
    print('Hello ' + name)

hello('zhang')
```

<br>

---

<br/>


## 返回值和return

用`def`语句创建函数时，可用`return`语句指定应该返回什么值。


<br>

---

<br/>


## None值

在Python中有一个值称为None，它表示没有值。None是None Type数据类型的唯一值（其它编程语言可能称这个值为null、nil或undefined）。
在幕后，对于所有没有return语句的函数定义，Python都会在末尾加上return None。


<br>

---

<br/>


## 关键字参数

**关键字参数**是由函数调用时加在它们前面的关键字来识别的。

如`print()`函数的`end`和`sep`关键字参数。你也可以在你编写的函数中添加关键字参数。

```py
print('A')
print('B')

print('A', end='')
print('B')

print('A', 'B', 'C')

print('A', 'B', 'C', sep='-')
```

<br>

---

<br/>


## 局部和全局作用域

在被调用函数内赋值的变元和容器，处于该函数的**局部作用域**。在所有函数之外赋值的变量，属于**全局作用域**。

虽然在小程序中使用全局变量没有太大问题，但当程序变得越来越大时，依赖全局变量就是一个坏习惯。

- 局部变量不能在全局作用域内使用
- 局部作用域 不能使用其它局部作用域内的变量
- 全局变量可以在局部作用域中读取
- 名称相同的局部变量和全局变量
    + 应该避免在不同作用域内使用相同变量名，虽然Python让局部变量和全局变量同名是完全合法的。


<br>

---

<br/>


## global语句

如果需要在一个函数内修改全局变量，就使用`global`语句。使用`global`先声明变量是全局变量，然后在对它进行修改。

```py
def spam():
    global name
    name = 'zhang'

name = 'acb'
sapm()
print(name)
#zhang
```


<br>

---

<br/>


## 异常处理

到目前为止，在Python中遇到错误或异常，意味着整个程序奔溃。我们不希望这发生在真实的程序中。相反，我们希望程序能检测错误，处理它们，然后继续运行。

错误可以由`try`和`except`语句来处理。那些可能出错的语句被放在`try`子句中。如果错误发生，程序执行就传到接下来的`except`字句开始处。

```py
def spam(number):
    try:
        return 42 / number
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(0))
print(spam(4))

```

