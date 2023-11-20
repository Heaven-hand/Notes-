#if 语句要注意缩进 空格和tab键不可以混用！
age = int(input('请输入年龄:'))
if age >= 18:
    print('yes')
else:
    print('no')

# not 可给当前的条件取反
ops = True
if not ops:
    print('yes')
else:
    print('no')
# if 的进阶使用
# if xxx:
#     print('')
# elif xxx:
#     print('')
# else:


# if 的嵌套用法 在前提条件的基础上再一次进行判断

# 随机数的用法
import random
print(random.randint(1, 4))
