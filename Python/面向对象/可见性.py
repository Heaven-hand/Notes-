class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course):
        print(f'{self.__name} is now learning {course}')

    # 读取私有属性
    @property
    def name(self):
        return self.__name

    # 修改私有属性
    @name.setter
    def name(self, name):
        self.__name = name or 'NONE'

    @property
    def age(self):
        return self.__age


stu1 = Student('alice', 18)
print(stu1.name, stu1.age)
stu1.name = "bob"
print(stu1.name)
# print(stu1.__name) 类内才能调用，私有的属性

# print(stu1.__Student.__name)
