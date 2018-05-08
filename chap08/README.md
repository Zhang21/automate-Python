# 读写文件


<br>


- 文件与文件路径
    + windows的反斜杠`\`与Linux的斜杆`/`
    + 当前工作目录
    + 绝对路径与相对路径
    + 用`os.makedirs()`创建新文件夹
    + `os.path`模块
    + 处理绝对路径和相对路径
    + 查看文件大小和文件夹内容
    + 检查路径有效性
- 文件读写过程
    + 用`open()`函数打开文件
    + 读取文件内容
    + 写入文件
- 用`shelve`模块保存变量
- 用`pprint.pformat()`函数保存变量
- 项目：生成随机的测验试卷文件
- 项目：多重剪贴板


<br>
<br/>

---

<br/>



## 文件与路径


当程序运行时，变量是保存数据的好方法，如果希望程序结束后数据仍然保持，就需要将数据保存到文件中。

注意windows和Unix-Like之间的差异。


<br>


### windows的反斜杠和Linux的斜杠


- 反斜杠`\`
- 斜杠`/`

在编写Python脚本的时候，请分区这两者的不同。

```py
import os

os.path.join('usr', 'bin', 'spam')
#'usr/bin/spam'




#栗子
import os

myFiles = ['1.txt', '2.txt', 'a.txt']
for file in myFiles:
    print(os.path.join('/tmp', file))

#/tmp/1.txt
#/tmp/2.txt
#/tmp/a.txt

```


<br>


### 当前工作目录


- `os.getcwd()`函数，取得当前工作目录
- `os.chdir()`函数，改变当前路径，更改的工作目录不存在的话，则会报错


```py
import os

os.getcwd()
#'/tmp'

os.chdir('/home')
os.getcdw()
#'/home'

```


<br>


### 绝对路径和相对路径


有两种方法指定一个文件的路径：

- **绝对路径(Absolute path)**
- **相对路径(Relative path)**
- `.`，当前目录
- `..`，上一级目录


<br>


### 创建新文件夹


- `os.makedirs()`函数，创建新文件夹

```py
import os

os.makedirs('/tmp/zhang')

```


<br/>


### `os.path`模块


- `os.path`模块，包含了许多与文件名和文件路径相关的有用函数。


<br>


### 处理绝对路径和相对路径


- `os.path.abspath()`，返回参数的绝对路径
- `os.path.isabs()`, 如果是一个绝对路径就返回True
- `os.path.repath(path, start)`，返回从start路径到path的相对路径
- `os.path.dirname()`，返回最后一个斜杠前的所有内容
- `os.path.basename()`，返回最后一个斜杠后的所有内容
- `os.path.split()`，返回一个路径的目录和基本名称
- `os.path.sep()`，分割

```py
import os

os.path.abspath('./zhang')
#'/tmp/zhang'

os.path.isabs('/tmp/zhang')
#True

os.path.isabs(os.path.abspath('./zhang'))
#True


os.path.relpath('/tmp/zhang', '/tmp')
#'zhang'


os.path.dirname('/tmp/zhang/1.txt')
#'/tmp/zhang'

os.path.basename('/tmp/zhang/1.txt')
#`1.txt`

os.path.split('/tmp/zhang/1.txt')
#('/tmp/zhang', '1.txt')

(os.path.dirname('/tmp/zhang/1.txt'), os.path.basename('/tmp/zhang/1.txt'))
#('/tmp/zhang', '1.txt')

```


<br>


### 查看文件大小和文件夹内容


- `os.path.getsize()`，返回参数文件的字节数
- `os.listdir()`，返回文件列表

```py
import os

os.path.getsize('/tmp/1.txt)
#4

os.listdir('/tmp')
#['1.txt', 'zhang']

```


<br>


### 检查路径有效性


如果你提供的路径不存在，Python函数就会崩溃并报错。

- `os.path.exists()`，检查文件夹或文件存在与否
- `os.path.isfile()`，检查是否为文件
- `os.path.isdir()`，检查是否为目录

```py
import os

os.path.exists('/tmp/zhang')
#True

os.path.isfile('/tmp/1.txt')
#True

os.path.isdir('/tmp/zhang')
#True

```


<br>
<br/>

---

<br>



## 文件读写过程


你可指定文件的位置，进行读写。
**纯文本文件**只包含基本字符，不包含字体、大小和颜色信息。

在Python中，读写文件有3个步骤：

- 调用`open()`函数，返回一个File对象
- 调用File对象的`read()`或`write()`方法
- 调用File对象的`close()`方法，关闭该文件


<br>


### 用Open()函数打开文件


向`open()`函数传递一个文件路径(绝对或相对)以打开文件，返回一个File对象。
这些命令将以纯文本文件的模式打开文件，简称为**读模式**。

```py
echo -e '1\n2\n3' > /tmp/1.txt

file = open('/tmp/1.txt')
#或
file = open('/tmp/1.txt', 'r')

```


<br>


### 读取文件内容


- `read()`方法，将整个文件内容读取为一个字符串值
- `readlines()`方法，将文件内容读取为一个字符串列表。列表中的每个字符串就是文本中的每一行

```py
file = open('/tmp/1.txt', 'r')
file.read()
#'1\n2\n3\n'


file.readlines()
#['1\n', '2\n', '3\n']

```


### 写入文件


如果打开文件时用读模式，则不能写入文件。需要以**写入纯文本模式**打开文件，或简称为**写模式**和**添加模式**。

- 写模式，覆盖原有文件
- 添加模式，向文件中添加内容


```py
file = open('/tmp/1.txt', 'w')
file.write('Hello world!\n')
file.close()


file = open('/tmp/1.txt', 'a')
file.write('Line2')
file.close()


file = open('/tmp/1.txt')
file.readlines()
#['Hello world!\n', 'Line2']

```


<br>
<br/>


## 用shelve模块保存变量


利用shelve模块，可将Python程序中的数据保存到二进制的shelf文件中。这样程序就可以从硬盘中恢复变量的数据。

```py
import shelve

shelFile = shelve.open('mydata')
alp = ['A', 'AA', 'AAA']
shelFile['alps'] = alp

shelFile.close()


shelFile = shelve.open('mydata')
shelFile['alps']
#['A', 'AA', 'AAA']

shelFile.close()

```


<br>
<br/>


## 用pprint.pformat()函数保存变量

`pprint.pformat()`函数将提供一个字符串，你可将它写入`.py`文件。该文件称为你自己的模块，如果需要存储在其中的变量，可以导入它。

```py
import pprint

cats = [ {'name': 'A', 'desc': 'a'}, {'name': 'B', 'desc': 'b'}  ]

pprint.pformat(cats)
#"[{'desc': 'a', 'name': 'A'}, {'desc': 'b', 'name': 'B'}]"

file = open('myCats.py', 'w')
file.write('cats = ' + pprint.pformat(cats) + '\n')
file.close()


import myCats

myCats.cats
#[{'name': 'A', 'desc': 'a'}, {'name': 'B', 'desc': 'b'}]

```






























































