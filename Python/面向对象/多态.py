# 面向对象的三大特性： 封装，继承，多态
# 多态就是不同的子类继承父类的方法执行后有不同的效果

class A(object):
    def work(self):
        print('working')


class B(A):
    def work(self):
        print('programing')


class C(A):
    def work(self):
        print('printing')


b = B()
c = C()
b.work()
c.work()