"""
定义函数求1-990的和，用for循环完成
"""


def sum(num):
    res = 0
    for i in range(num + 1):
        res += i
        i += 1
    print(res)


sum(990)


