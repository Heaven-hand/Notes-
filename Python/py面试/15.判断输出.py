# 1
class Foo:
    def __f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.__f1()  # 封装过了，一开始名字就已经变化了，意味这个函数是Foo的私有函数，还是调用__f1()


class Bar(Foo):
    def __f1(self):
        print('Bar.f1')


obj = Bar()
obj.f2()

# 2
