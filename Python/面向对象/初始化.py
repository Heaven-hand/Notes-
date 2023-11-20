class Student:
    # 初始化
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def study(self, course):
        # 属性使用self进行调用，参数是直接调用的
        print(f'{self.name} are now learning {course}')

    def play(self):
        print(f'{self.name} are now playing games')

    # 使用内置的函数
    def __repr__(self):
        return f'{self.name} : {self.age}'


# 实例化
stu1 = Student('alice', 18)
stu2 = Student('bob', 20)
print(stu1)  # 使用上面的魔术方法repr后就可以不返回内存地址
stu1.study('py')
stu2.play()
