# 字符串的使用，使用+进行字符的拼接
first_name = "xiao"
last_name = "ming"
print(first_name + last_name)

# 使用input 函数进行变量的输入
data1 = input('please input a number: ')
data2 = input('please input a number: ')
price = float(data1)
weight = float(data2)
print(price * weight)

# -------------------------变量的格式化输出-----------------
name = 'xiaoming'
student_number = 1
price = float(input('please input the price:'))
weight = float(input('please input the weight:'))
money = price * weight
print('the price is %.2f,weight %.2f, total money is %.2f' % (price, weight, money))
print('my name is %s' % name)
print('my student number is %06d' % student_number)
scale = 10.23
print('%.2f%%' % (scale * 100))  # 两个%打印%
