class Student:
    __slots__ = ('name', 'age')  # 如果当前的类不允许动态添加属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('alice', 30)
# 在不修改的前提下，添加属性
# stu.sex = 'male'
# print(stu.name, stu.age, stu.sex)
