"""
迭代是Python最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器：


如果一个对象有__iter__(),那么他是可迭代的iterable
如果一个可迭代的对象有__next__(),那么他就是迭代器，for循环的实现就是这样的。

列表是可迭代的，但是不是迭代器，可以用iter()构造迭代器。
next() == __next__()


每一次迭代器都弹出一个数，这样在处理规模较大的数据的时候就会节省内存，这种特性也叫作惰性加载
"""


# import sys
#
# list = [1, 2, 3, 4]
# it = iter(list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
# for i in it:
#     print(f'{i:.1f}')
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


# 把一个类作为一个迭代器
class MyNumbers:

    def __init__(self):
        self.a = 1

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
# myiter = iter(myclass)

print(next(myclass))


from collections.abc import Iterator
print(isinstance(myclass, Iterator))

from collections.abc import Iterable
print(isinstance(myclass, Iterable))

# 翻转
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


r = Reverse('abc')
for i in r:
    print(i)
