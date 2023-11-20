class A:
    # 创建类的属性
    def __init__(self):
        self.num_1 = 100
        self.__num_2 = 200

    def __test(self):
        print(f'{self.num_1}, {self.__num_2}')

    def test(self):
        print(f'{self.__num_2}')
        self.__test()


class B(A):

    def demo(self):
        print(f'{self.num_1}')


# 父类中的私有方法也是不允许子类直接进行调用的
b = B()
print(b)
print(b.num_1)
b.demo()
b.test()  # 利用父类的公有方法可以间接访问到私有属性以及私有的方法
# 私有属性没有办法打印
# b.demo()
