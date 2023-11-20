"""
生成器的本质也是迭代器
"""


def func():
    j = 1
    for a in range(3):
        yield j
        j += 1


# 创建生成器对象
# 生成器内部也有迭代器的方法iter和next
obj1 = func()
for i in obj1:
    print(i)
