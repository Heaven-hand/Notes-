i = 1
while i <= 5:
    print('hello python')
    i += 1
print('循环结束后i的值为%d' % i)
# 注意修改循环的结束条件，防止死循环


# break 是跳出整个循环
# continue 是跳出一次，剩下的继续生效


row = 0
while row <= 5:
    print('*' * row)
    row += 1

for i in range(3):
    print('a')
    i+=1