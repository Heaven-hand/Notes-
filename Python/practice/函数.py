# name = 'bob'
#
#
# def hello():
#     """
#     函数的注释
#     :return:
#     """
#     print('hello1')
#     print('hello2')
#     print('hello3')
#
#
# hello()
# print(name)


# # 函数参数的使用
# def sum_1():
#     num1 = 10
#     num2 = 20
#     res = num1 + num2
#     print('%d + %d = %d' % (num1, num2, res))
#
#
# sum_1()

#
# def sum_2(num1, num2):
#     res = num1 + num2
#     print('%d + %d = %d' % (num1, num2, res))
#
#
# sum_2(50, 20)


# def sum_3(num1, num2):
#     return num1 + num2
#
#
# # return后面的代码都不会执行
#
# res = sum_3(20, 30)
# print(res)


# 函数嵌套
def test_1():
    print('*' * 10)
    print('test1')
    print('*' * 10)


def test_2():
    print('-' * 10)
    print('test2')
    test_1()


test_2()