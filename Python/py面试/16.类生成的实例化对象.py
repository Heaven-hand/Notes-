class Foo:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):  # 在对象被调用的时候会自动触发该方法
        print(self, args, kwargs)


obj = Foo(1, 2)
obj(1, 2, 2, a=3, b=4)
