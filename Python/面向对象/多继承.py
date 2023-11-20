# 子类可以继承多个父类
class A:
    def test(self):
        print('test')


class B:
    def demo(self):
        print('demo')


class C(A, B):
    pass


# 如果子类继承了多个父类，并且多个父类中含有同名的方法（该情况在开发中应该注意避免）
# 在子中的调用顺序和继承声明的顺序有关（父类中的方法有重名）

c = C()
c.test()
c.demo()
