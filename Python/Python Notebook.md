# Python Notebook<入门到实践>

课后练习：https://github.com/OctopusLian/Python-Crash-Course-Homework



在考虑如何实现一个功能之前，先严格地列出这个功能能做什么，这能帮助我们在编程时把精力花在该花的地方

## 数据类型

- [ ] 数字
- [ ] 字符串
- [ ] 元组
- [ ] 列表
- [ ] 字典
- [ ] 集合

## 运算符

- [ ] 赋值
- [ ] 比较
- [ ] 逻辑
- [ ] 位
- [ ] 算数
- [ ] 成员

## 结构控制语句

- [ ] 条件
- [ ] 循环

## 类与函数

- [ ] 定义
- [ ] 参数
- [ ] 调用

## 模块

- [ ] 引用
- [ ] 属性

## 异常

- [ ] 常见异常

  ```py
  SyntaxError: invalid syntax #语法错误
  ```

  ```py
  IndentationError: unexpected indent #多余的缩进
  ```

  

- [ ] 抛出异常

- [ ] 捕获与处理

## 迭代器与生成器

## 文件读写

## 1.变量&数据类型

- 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打
  头
- 变量名不能包含空格，但可使用下划线来分隔其中的单词
- 不要将Python关键字和函数名用作变量名
- 慎用小写字母l和大写字母O
- 应使用小写的Python变量名

#### 字符串

python对于字符串的方法（方法是Python可对数据执行的操作）

```py
name = "ada lovelace"
print(name.title())	#title()以首字母大写的方式显示每个单词
#Ada Lovelace
```

```py
print(name.upper())
print(name.lower())
```

**存储数据时**，方法$lower()$很有用。很多时候，你无法依靠用户来提供正确的大小写，因此
需要将字符串先转换为小写，再存储它们。以后需要显示这些信息时，再将其转换为最合适的大
小写方式。



**字符的拼接**

```py
full_name = first_name + " " + last_name #   + 可以满足字符串的拼接功能
```

**字符串的输出格式**

```py
\n #换行
\t #空白缩进
```

**删除空白**

```py
favorite_language.rstrip() #执行删除空白的操作，但是没有保存结果
favorite_language = favorite_language.rstrip()#存回变量中
favorite_language.lstrip()#删除左端的空白
favorite_language.strip()#删除两端的空白
```

## 2.列表简介

Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。如果直接输出列表，则会包含['']在内的所有信息。在输出有特定要求的情况下应利用索引访问列表中的元素。

```py
print(bicycles[0].title()) #输出列表中的第一个信息并首字母大写进行输出
print(bicycles[-1].title())#输出最后一个元素 
```

注：该种约定适用于其他的**负数索引**（-2, -3... ... ）对于长度未知的列表是很便捷的输出方式

#### 1)**列表的插入**

```py
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#output
#['honda', 'yamaha', 'suzuki']
```

$append()$会将元素插入到列表的末尾（类似队列结构）

```py
motorcycles.insert(0, 'ducati') #选择位置进行插入
print(motorcycles)
#['ducati', 'honda', 'yamaha', 'suzuki']
```

方法$insert()$在索引0处添加空间，并将值'ducati'存储到这个地方。这种操作将列表中既有的每个元素都右移一个位置。

#### 2)**已知元素索引位置的删除**

```py
del motorcycles[0]  #如果知道要删除的元素在列表中的位置，可使用del语句。
```

删除之后将无法访问该数据

#### 3)**删除列表中最后一个位置的数据（类似stack）**

方法pop()可删除列表末尾的元素，并让你能够接着使用它。类似于弹出栈顶的元素。

```py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() #你可以使用他的元素值
print(motorcycles)
print(popped_motorcycle)
```

```py
first_owned = motorcycles.pop(0) #同理，只要知道了元素的索引位置，就可以选择位置进行弹出
```

注：如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用 $del$ 语句；如果你要在删除元素后还能继续使用它，就使用方法 $pop()$ 。

#### 4)**未知索引删除元素**

```py
motorcycles.remove('ducati')
print(motorcycles)
```

如果要使用被删除元素的值，请提前保存在某个变量中。

方法 $remove()$ 只能删除“一次”，因此如果列表中存在多个重复的元素值，则需要利用循环来确定是否将所有的该元素都删除了。

#### 5)**对列表进行排序**

```py
.sort()#排序之后会改变列表的内容（顺序）
cars.sort(reverse=True)#进行反向排序
```

**修改是永久性的**

```py
sorted()#临时排序，返回的是列表
sorted(iterable, cmp=None, key=None, reverse=False)# cmp是比较的方法
```

**倒序**

```py
cars.reverse() #仅仅是倒序进行输出，并没有进行排序
```

## 3.操作列表

#### 1)遍历列表

```py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
```

这些命名约定有助于你明白for循环中将对每个元素执行的操作。使用**单数和复数式名称**，可帮助你判断代码段处理的是单个列表元素还是整个列表。

#### 2)创建数值列表

```py
range(1,5) #1,2,3,4 
```

```py
numbers = list(range(1,6)) #将数字保存为列表形式
print(numbers)
#[1, 2, 3, 4, 5]
```

```py
even_numbers = list(range(2,11,2)) #指定步长进行数值的创建
print(even_numbers)
#[2, 4, 6, 8, 10]
```

创建某个数值列表的实例：

```py
squares = []
for value in range(1,11):
	squares.append(value**2)
```

#### 3)用列表解析的方式，更为简洁地生成目标列表：

```py
squares = [value**2 for value in range(1,11)]
```

进行统计计算的简单函数：

```py
min(digits)
max(digits)
sum(digits)
```

#### 4)切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，Python
在到达你**指定的第二个索引前面的元素后停止**

```py
#左侧是开始索引（空则为0），右侧是结束索引的下一个索引（空为输出到结尾）
players[0:3]
players[:3]
players[2:3]
players[2:]
players[-3:]# 最后三个
```

切片的遍历

```py
for player in players[:3]:#只遍历前三个元素
```

复制列表

要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。
这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。

```py
friend_foods = my_foods[:]
```

```py
friend_foods = my_foods
```

若不使用切片进行列表的复制：两个变量（列表）是**关联**的，因此对其中任何一个变量进行操作，两个列表的内容是同步改变的。而用切片的方式建立列表是构建了列表的一个**副本**，对变量的操作是不同步发生改变的。

#### 5)元组

Python将不能修改的值称为不可变的，而**不可变的列表被称为元组**。

```py
#'tuple' object does not support item assignment
dimensions = (200, 50) #使用圆括号进行元组的构建
dimensions[0] = 250 #这个是非法操作，因为不能对元组元素进行更改
dimensions = (400, 100)#这个操作是合法的，给元组变量赋值是合法的
```

如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。

#### 6)设置合适的代码格式 PEP8

每级缩进都使用四个空格。你在编写代码时应该使用制表符键，但一定要对编辑器进行设置，使其在文档中插入空格而不是制表符。

每行不超过80字符

注释的行长都不超过72字符

设置一个视觉标志——通常是一条竖线

## 4.If语句

在Python中检查是否相等时**区分大小写**

```py
>>> car = 'Audi'
>>> car == 'audi'
False
```

```py
>>> car = 'Audi'
>>> car.lower() == 'audi'#不会更改car的内容
True
```

检查特定值是否包含在列表中

```py
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

检查特定值是否不包含在列表中

```py
not in
```

**if-elif-else 结构: 可以使用多个elif，也可以省略else**

对列表进行循环操作之前**确定列表不是空的**

## 5.字典

在Python中，字典是一系列**键—值对**。每个键都与一个值相关联，你可以使**用键来访问**与之
相关联的值。与键相关联的值可以是**数字、字符串、列表乃至字典**。事实上，**可将任何Python对**
**象用作字典中的值。**在Python中，字典用放在花括号{}中的一系列键—值对表示

```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])#利用键来访问值
```

添加键—值对

```py
alien_0['x_position'] = 0
```

使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，通常都需要先
定义一个空字典。

```py
alien_0 = {}
```

删除键—值对

对于字典中不再需要的信息，可使用del语句将相应的键—值对**彻底删除**。使用del语句时，
必须指定字典名和要删除的键。

```py
del alien_0['points']
```

由类似对象组成的字典

```py
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
```

#### 1)遍历字典

**遍历所有的键—值对**

```py
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for key, value in user_0.items(): #.items()方法，它返回一个键—值对列表
	print("\nKey: " + key)
	print("Value: " + value)
```

注意，即便遍历字典时，**键—值对的返回顺序也与存储顺序不同**。Python不关心键—值对的存
储顺序，而只跟踪键和值之间的关联关系。

使用更符合语境的循环变量，将有利于代码的阅读

**遍历字典中的所有键**

```py
for name in favorite_languages.keys():#使用.keys()方法，也可以省略，输出的结果会是相同的
	print(name.title())
```

方法keys()并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键。字典→列表

**按顺序遍历字典中的所有键**

```py
for name in sorted(favorite_languages.keys()):#利用列表的排序
	print(name.title() + ", thank you for taking the poll.")
```

**遍历字典中的所有值**

```py
.values()
```

这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，
但如果被调查者很多，最终的列表可能包含大量的重复项。为剔除重复项，可使用集合（set）。
集合类似于列表，但每个元素都必须是独一无二的：

```py
set(favorite_languages.values())
```

字典列表嵌套

列表字典嵌套

字典字典嵌套（最好是键一样，否则循环遍历的时候将十分复杂）

## 6.用户输入&while循环

#### 1)用户输入

```py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

输入提示最好加一个空格，这样用户的交互会更加清晰

有时候，提示可能超过一行，例如，你可能需要指出获取特定输入的原因。在这种情况下，可将提示存储在一个变量中，再将该变量传递给函数input()。这样，即便提示超过一行，input()语句也非常清晰。

```py
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
```

注：用户输入得到的结果是字符串形式的，如果想要利用其作为数值表示，则要使用 $int()$ 进行转换

#### 2)while循环

for循环针对的是集合中所有元素都要运行的代码块，while循环则是一个不断运行直到条件不满足为止。

#### 3)使用标志

当while循环需要多个判断条件来确定其运行状态时，可以使用标志来对while循环进行规制。

```py
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

注：在任何Python循环中都可使用break语句进行提前退出

**在循环中使用continue**

```py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
    	continue
    print(current_number)
```

**continue的作用是跳过下面的代码**，直接回到循环开始的部分

#### 4)使用while 循环来处理列表和字典

for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。要在**遍历列表的同时对其进行修改，可使用while循环**。通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。

**在列表之间移动元素**

```py
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users: #这样可以将列表中的内容进行移动，空则停止（对于链表也是同样的道理）
```

**删除包含特定值的所有列表元素**

```py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
```

## 7.函数

文档字符串（docstring）的注释，描述了函数是做什么的。

```py
"""函数功能注释"""
```

#### 1)实参和形参

```py
def get_name(username):
	... ...
get_name('YOU')
```

上面的例子中' YOU '就是一个实参（实际的参数），在调用函数的时候被传递给形参username。

#### 2)传递实参

**位置实参**

顺序是最重要的，实参和形参的顺序要一一对应

**关键字实参**

使用关键字实参时，务必准确地指定函数定义中的形参名。

```py
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

**默认值**（**这样可以将实参变成可选的项**）

```py
def describe_pet(pet_name, animal_type='dog'):#注意：缺省的形式参数要放在最后面
```

对于传递列表参数

```py
function_name(list_name[:])
```

可以使用列表的副本进行传递，这样原始的列表内容就不会被修改

**传递任意数量的实参**

```py
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

这个形参的含义是**创建了一个元组**，Python将实参封装到一个元组中，即便函数只收到一个值也如此

如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

```py
def make_pizza(size, *toppings):
```

```py
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)
```

这个形参的含义是**创建了一个字典**，可将函数编写成能够接受任意数量的键—值对。

#### 3)将函数存储在模块中

使函数模块化，与主程序分离。主程序只需要import这个函数模块就可以使用对应的功能，可以在编程的时候实现更宏观的视角。

要让函数是可导入的，得先创建模块。模块是扩展名为 $.py$ 的文件，包含要导入到程序中的代码。

这就是一种导入方法：只需编写一条import语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。如果你使用这种import语句导入了名为module_name.py的整个模块，就可使用下面的语法来使用其中任何一个函数：

```py
module_name.function_name()
```

```py
from module_name import function_name#导入模块中的特定函数
from module_name import function_0, function_1, function_2
```

以上调用的时候可以直接使用对应的函数名，而不需要使用“.”来引入

```py
from module_name import function_name as fn #为指定的函数申请别名
import module_name as mn                    #也可以为指定的模块申请别名
```

```py
from module_name import * #导入模块中的所有函数
```

由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法：如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：Python可能遇到多个名称相同的函数或变量，进而覆盖函数

最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。这能让代码更清晰，更容易阅读和理解。

#### 4)函数编写指南

- 应给函数指定描述性名称，且只在其中使用**小写字母和下划线**。

- 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用**文档字符串格式**。

- 给形参指定默认值时，等号两边不要有空格：

  ```py
  def function_name(parameter_0, parameter_1='default value')
  ```

- 对于函数调用中的关键字实参，也应遵循这种约定：

  ```py
  function_name(value_0, parameter_1='value')
  ```

- 文件的开头可以使用注释对其进行描述，然后是引入模块，然后是函数实现，最后是函数主体。

## 8.类

面向对象编程：编写表示现实世界中的事物和情景的类，根据类来创建对象被称为**实例化**

#### 1)创建和使用类

根据约定，在Python中，首字母大写的名称指的是类。这个类定义中的括号是空的，因为我们要从空白创建这个类。

```py
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
```

**方法 _ _init()_ _** 

类中的函数称为方法，在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。**根据类创建实例的时候python都会自动运行他。**

在这个方法的定义中，**形参self必不可少**，**还必须位于其他形参的前面**。

为何必须在方法定义中包含形参self呢？

因为python在调用init创建实例的时候会自动传入实参self，每个与类相关联的方法调用都自动传递实参self，**它是一个指向实例本身的引用**，让实例能够访问类中的属性和方法。

每当我们根据Dog类创建实例时，**都只需给最后两个形参（name和age）提供值。**

**以self为前缀的变量都可供类中的所有方法使用**，我们还可以通过类的任何实例来访问这些变量。

#### 2)根据类创建实例

可将类视为有关如何创建实例的说明

```py
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
```

inti函数并未显式地包含return语句，但Python自动返回一个表示这条小狗的实例。

根据python编程中的约定，大写字母开头的变量表示类，小写字母对应其中的实例。

传入实参之后，我们就可以使用类中对应的属性以及函数。

**访问属性**

```py
my_dog.name #利用句点表示法
```

**调用方法**

同理

**总结**

可按需求根据一个类创建任意数量的实例，条件是将每个实例都存储在不同的变量中，或占用
列表或字典的不同位置。

#### 3)使用类和实例

```py
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法__init__()内指定这种初始值是可行的；如果你对某个属性这样做了，就无需包含为它提供初始值的形参。

#### 4)修改属性的值

**直接修改属性的值**

```py
my_new_car.odometer_reading = 23
```

有时候需要像这样直接访问属性，但其他时候需要编写对属性进行更新的方法。

**通过方法修改属性的值**

无需**直接访问属性**，而可将值传递给一个方法，由它在内部进行更新。

```py
def update_odometer(self, mileage):
    """将里程表读数设置为指定的值"""
    self.odometer_reading = mileage
```

可以添加一些逻辑，禁止任何人将里程表读数往回调。

**通过方法对属性的值进行递增**

```py
+=
```

可以使用类似于上面的方法来控制用户修改属性值（如里程表读数）的方式，但能够访问程序的人都可以通过直接访问属性来将里程表修改为任何值。要确保安全，除了进行类似于前面的基本检查外，还需特别注意细节。

#### 5)继承

编写类时，并非总是要从空白开始。如果要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，而**新类称为子类**。子类继承了其父类的所有属性和方法，**同时还可以定义自己的属性和方法**。

```py
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

**创建子类时，父类必须包含在当前文件中，且位于子类前面**

super()是一个特殊函数，帮助Python将父类和子类关联起来。父类也称为超类（superclass），名称super因此而得名。让ElectricCar实例包含父类的所有属性。

**重写父类的方法**

直接重新进行同名方法的定义即可。

**将实例用作属性**

给类添加的细节越来越多：属性和方法清单以及文件都越来越长。在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。你可以**将大型类拆分成多个协同工作的小类。**

```py
class Battery():
"""一次模拟电动汽车电瓶的简单尝试"""
def __init__(self, battery_size=70):
    """初始化电瓶的属性"""
    self.battery_size = battery_size
    def describe_battery(self):
    """打印一条描述电瓶容量的消息"""
    print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```

最后一行就是将新的类作为属性的赋值

#### 6)导入类

导入类是一种有效的编程方式，还是使用import

```py
from car import Car
```

可根据需要在一个模块中存储任意数量的类

导入多个类：

```py
from car import Car, ElectricCar
```

导入整个模块

```py
import car
```

导入模块中的所有类

```py
from module_name import *
```

需要从一个模块中导入很多类时，最好导入整个模块，并使用 $modulename.classname$ 语法来访问类。这样做时，虽然文件开头并没有列出用到的所有类，但你清楚地知道在程序的哪些地方使用了导入的模块；你还避免了导入模块中的每个类可能引发的名称冲突。

#### 7)python标准库

```py
from collections import OrderedDict
favorite_languages = OrderedDict()#利用OrderedDict构建有序的空字典，这样键值对的输出排列就和建立的时候是一样的。
```

#### 8)编码风格

- 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线
- 实例名和模块名都采用小写格式，并在单词之间加上下划线
- 在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类
- 先编写导入标准库模块的import语句，再添加一个空行，然后编写导入你自己编写的模块的import语句

## 9.文件与异常

#### 1)文件读取

```py
with open('pi_digits.txt') as file_object:#with已经负责进行文件的关闭了
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())
```

Python在当前执行的文件所在的目录中查找指定的文件

关键字with在不再需要访问文件后将其关闭。也可以调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭。这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。如果在程序中过早地调用close()，你会发现需要使用文件时它已关闭（无法访问），这会导致更多的错误。并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可让Python去确定：你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。

read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。要删
除多出来的空行，可在print语句中使用rstrip()

**文件路径**

```py
'''In Linux'''
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:
```

```py
'''In Windows'''
file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:
```

Linux 中使用的是斜杠(/)，Windows中使用的是反斜杠(\)

#### 2)逐行读取

```py
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
    print(line)
```

每行的末尾都有一个看不见的换行符

创建一个文件内容逐行的列表

```py
with open(filename) as file_object:
	lines = file_object.readlines()
```

利用readlines()方法可以实现逐行读取并且存储在列表中

可以使用切片的方法只输出字符串前面的某些部分

#### 3)写入文件

```py
filename = 'programming.txt'
with open(filename, 'w') as file_object:
	file_object.write("I love programming.")
```

实参（'w'）告诉Python，我们要以写入模式打开这个文件。打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）。如果你省略了模式实参，Python将以默认的只读模式打开文件。

注：**Python只能将字符串写入文本文件**。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。

要让每个字符串都单独占一行，需要在write()语句中包含换行符（'\n'）

指定了实参'a'，以便将内容**附加到文件末尾**，而不是覆盖文件原来的内容

#### 4)异常

try-except-else代码块的工作原理大致如下：Python尝试执行try代码块中的代码；**只有可能引发异常的代码才需要放在try语句中**。有时候，有一些仅在try代码块成功执行时才需要运行的代码；这些代码应放在else代码块中。except代码块告诉Python，如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。

```py
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
    	break
    second_number = input("Second number: ")
    try:
    	answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
    	print("You can't divide by 0!")
    else:
    	print(answer)
```

设置异常的好处：traceback不会向用户显示，提高了代码的健壮性（因为traceback的提示信息中不仅仅包含文件名，还包含其所属路径，会向攻击者暴露代码的漏洞）

#### 5)分析文本

```py
>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']
```

方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点

```py
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
        	contents = f_obj.read()
    except FileNotFoundError:#对文件不存在进行异常的处理
    	msg = "Sorry, the file " + filename + " does not exist."
    	print(msg)
    else:
    # 计算文件大致包含多少个单词
    	words = contents.split()
    	num_words = len(words)
    	print("The file " + filename + " has about " + str(num_words) +
    	" words.")
```

```py
except FileNotFoundError:
	pass
```

pass可以让python在发生错误的时候什么也不做。pass语句还充当了**占位符**，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么

#### 6)存储数据

程序把用户提供的信息存储在列表和字典等数据结构中。用户关闭程序时，你几乎总是要保存他们提供的信息；一种简单的方式是使用模块json来存储数据。模块json让你能够将简单的Python数据结构转储到文件中，并在程序**再次运行时加载该文件中的数据**。你还可以使用json在Python程序之间分享数据。更重要的是，**JSON数据格式并非Python专用的**，这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。

注：**JSON（JavaScript Object Notation）**格式最初是为JavaScript开发的，但随后成了一种常见格式，被包括Python在内的众多语言采用。

```py
#write
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)#将numbers存入f_obj
```

```py
#load
import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)
```

这是一种在程序之间共享数据的简单方式

下面给出一个记录单一用户的读写代码：

```py
import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")
```

#### 7)重构

将代码**划分为一系列完成具体工作的函数**。这样的过程被称为重构。重构让代码更清晰、更易于理解、更容易扩展。

## 10.测试代码