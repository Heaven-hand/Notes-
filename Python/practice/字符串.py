string = 'hello world'
for i in string:
    print(i)

print(string[1])
print(string[1:])  # 切片
print(string[1:4])  # ell

print(string.capitalize())
print(string.upper())
print(string.title())

print(string.find('o'))  # 没有的话会返回-1
print(string.index('o'))  # 没有会报错

print(string.find('o',5))  # 限定位置查找

print(string.rfind('o'))  # 从后往前找

print(string.startswith('Hell'))  # 区分大小写
print(string.endswith('a'))

s2 = '1234'
print(s2.isdigit())  # 纯数字组成
print(s2.isalpha())
print(s2.isalnum())  # 数字或字母的组合

s3 = 'hello'
print(s3.center(20,'@'))
print(s3.ljust(20))
print(s3.rjust(20))
print(s3.zfill(20))
print('-33'.zfill(5))

# 格式化输出
a = 321
b = 123
c = 123456789
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')  # 最新的格式化方法 py3.6以后版本使用
print(f'{c:,}')
print(f'{a:.2%}')
print(f'{a:+.2f}')
print(f'{a:0>10d}')
print(f'{a:.2e}')


s4 = '    jkhdfkshi    \t'
print(s4.strip())

print(s4.replace('k', '@', 1))  # 后面是替换的次数

s5 = 'I owe you'
s6 = s5.split()
print(s6)  # 变成列表
# print(''.join(s5))
print('@'.join(s6))  # 对列表进行操作

s7 = 'I$owe$you$so$much'
print(s7.split())  # 默认拆分的是空格
print(s7.split('$'))
print(s7.split('$', 2))  # 定义拆分的次数


s8 = '面试'
a = s8.encode('utf-8')
b = s8.encode('gbk')
print(a)
print(b)
c = a.decode('utf-8')
print(c)
d = a.decode('gbk')
print(d)  # 解码的字符集不一样会出现乱码