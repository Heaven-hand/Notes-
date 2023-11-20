# 代码重复的利用
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print('eat')
#     def run(self):
#         print('run')
#
#     def sleep(self):
#         print('sleep')
#     def drink(self):
#         print('drink')
#
# class Dog:
#     def eat(self):
#         print('eat')
#     def run(self):
#         print('run')
#
#     def sleep(self):
#         print('sleep')
#     def drink(self):
#         print('drink')
#     def bark(self):
#         print('bark')

# dog = Animal()

# 当父类的方法不能进行满足子类的需求时，可以进行重写override
class Animal:  # 父类
    def eat(self):
        print('eat')

    def run(self):
        print('run')

    def sleep(self):
        print('sleep')

    def drink(self):
        print('drink')


class Dog(Animal):  # 子类继承父类，从基类Animal派生出来
    def bark(self):
        print('bark')


class SuperDog(Dog):
    def fly(self):
        print('fly')

    def bark(self):  # 子类中的重写，和父类中的方法是同名的
        print('super bark')
        super().bark()  # super是可以继续使用父类的方法的对象
        Dog.bark(self)  # python 2.x

class Cat(Animal):
    def catch(self):
        print('catch')


doggy = SuperDog()
doggy.drink()
doggy.bark()
catty = Cat()
catty.catch()
# 面向对象的继承有传递性
