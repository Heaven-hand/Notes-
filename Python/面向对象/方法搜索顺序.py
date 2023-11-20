# MRO  method resolution order
class A:
    def test(self):
        print('test')


class B:
    def demo(self):
        print('demo')


class C(A, B):
    pass


c = C()
c.test()
c.demo()
print(C.__mro__)

"""
调用C类的时候，会寻找内部是否有这个方法，然后是A, B,最后是基类
"""