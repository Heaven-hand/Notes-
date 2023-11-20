# pyhton3中的类都是新式类（如果不明确继承的类）
class A(object):  # 提高代码的兼容性，python2.x也可以运行
    pass


print(dir(A))  # object 中包含的方法


class B:
    pass


print(dir(B))
