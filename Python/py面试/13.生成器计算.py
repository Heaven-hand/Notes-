# # 非生成器
#
# def func(num):
#     res = 1
#     for i in range(num):
#         res *= (i + 1)
#
#     return res
#
#
# def result(num):
#     res = 0
#     for i in range(num):
#         res += func(i + 1)
#     return res
#
#
# print(result(4))


def func(num):
    i = 1
    j = 1
    while i <= num:
        yield j  # 生成器的标志， 意味着j是可以迭代的
        i += 1
        j = i * j


res = 0
for i in func(4):
    res += i
print(res)
