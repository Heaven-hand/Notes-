print('hello world!')
print ('开始py的学习')  # python3是支持中文的，但是python2不支持
"""
多行注释
"""

# --------------------------算数运算符号
# 幂运算优先级最高，乘除取余一样，最后是加减，比较，等于，赋值，逻辑
a=10+20
print(a)

b=10-20
print(b)

c=10*20
print(c)
# 单反斜杠除，小数
d=10/20
print(d)
# 双反斜杠，取整数
e=10//20
print(e)
# 取余
f=9%2
print(f)

g=2**3
print(g)
# 输出5个-
print('-----')
print('-'*5)

# 赋值运算符：上述的运算符都可以进行整合变成赋值运算符 作用是简化
a = 1
if a == 1:
    a += 1
    print(a)

n = 0
x = 100
while n<float('inf'):
    if n*n >= x:
        print(n)
        break
    else:
        n+=1