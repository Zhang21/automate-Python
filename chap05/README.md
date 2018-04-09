# 字典和结构化数据


- 字典数据类型
    + 字典与列表
    + keys(), values()和items()方法
    + 检查字典中是否存在键或值
    + get()方法
    + setdefault()方法
- 漂亮打印
- 使用数据结构对真实世界建模
    + 井字棋盘
    + 嵌套的字典和列表


<br>
<br/>

---

<br>


## 字典数据类型


字典数据类型，提供了一种灵活的访问和组织数据的方式。
像列表一样，**字典**是许多值的集合。但不像列表的下标，字典的索引可以使用许多不同数据类型。
字典的索引被称为**键**，键及其关联的值称为**键-值**对。
字典使用花括号`{}`。

```py
#将字典赋值给myCat变量
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

#键：'size', 'color', 'gray'
#值：'fat', 'gray', 'loud'


#访问
myCat['size']
#'fat'
```

<br>


### 字典与列表

字典里的表项是不排序的，键-值对输入的顺序并不重要。你可以用任意值作为键。
访问字典中不存在的键，会导致KeyError错误。

```py
dicA = {'name': 'zhang', 'sex': 'male', 'age': '18'}
dicB = {'age': '18', 'name': 'zhang', 'sex': 'male'}

dicA == dicB
#True
```


<br>


### keys(), values()和items()方法

有3种字典方法：

- `keys()`, 返回字典的**键**
- `values()`, 返回字典的**值**
- `items()`, 返回字典的**键-值**

```py
dic = {'name': 'zhang', 'sex': 'male', 'age': '18'}

for k in dic.keys():
    print(k)
#name
#sex
#age

for v in dic.values():
    print(v)
#zhang
#male
#18

for i in dic.items():
    print(i)
#('name', 'zhang')
#('sex', 'mali')
#('age', '18')

for k, v in dic.items():
    print('Key is: ' + str(k) + ' Value is: ' + str(v))
#Key is: name Value is: zhang
#...

```


<br>


### 检查字典中是否存在键或值

- `in`
- `not in`

```
dic = {'name': 'zhang', 'sex': 'male', 'age': '18'}

'name' in dic.keys()
#True
'zhang' in dic.values()
#True

```


<br>


### get()方法

`get()`方法，有两个参数。一个是字典的键，一个是备用值(即该键不存在时返回的值)。

```py
dic = {'name': 'zhang', 'sex': 'male', 'age': '18'}

print(str(dic['NAME']))
#KeyError

print(str(dic.get('NAME', 'backupValue')))
#'backupValue'

```
    

<br>


### setdefault()方法










