class T(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # 装饰器
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     return a + b > c and a + c > b and b + c > a
    # 静态方法不和当前类帮定，类方法是需要声明作用类的cls
t = T(3, 4, 5)
print(T.is_valid(3, 4, 5))
# 在调用静态的方法时不需要进行实例化