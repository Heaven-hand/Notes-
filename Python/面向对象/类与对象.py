class Student:
    # 函数在类之中，被称为类的方法
    def study(self, course):
        print(f'now learning {course}')

    def play(self):
        print('now play')


stu_1 = Student()  # 实例化2
stu_2 = Student()
# # 输出内存的地址，16进制
# print(stu_1)
# print(stu_2)
#
# print(hex(id(stu_1)), hex(id(stu_2)))

# 通过对象.方法进行调用
stu_1.study('py')

# 需要对当前的类进行实例化
Student().study('java') # 实例化1