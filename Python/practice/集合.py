# 无序性 互异性 确定性
# 集合底层的存储特性是哈希存储，集合成员的运算性能要优于列表，不能用索引来确定
set2 = {1, 2, 3, 3, 3}
print(set2)

set1 = set('hello')
print(set1)

list_data = [1, 2, 3, 3]
print(set(list_data))

set3 = {num for num in range(1, 20) if num % 5 == 0}
print(set3)

for i in set3:
    print(i)


# 成员运算
set4 = {1, 2, 3, 4}
print(10 in set4)
print(1 in set4)
set5 = {'py', 'c', 'go'}
print('py' in set5)
print("py" not in set5)

# 交并差运算
set6 = {2, 3}
print(set4 & set6)  # 交集
print(set4 | set6)  # 并集
print(set4 - set6)  # 未出现过的
print(set4 ^ set6)  # 对称差

print(set4 > set6)  # 超集
print(set6 < set4, set6 <= set4)  # 真子集和子集

set_1 = set()
set_1.add(33)
set_1.add(55)
set_1.add(66)
set_1.update({1, 2, 3})
print(set_1)

set_1.discard(33)
print(set_1)
if 1 in set_1:
    set_1.remove(1)

print(set_1)
set_1.pop()
print(set_1)

print(set1.isdisjoint(set_1))  # 没有想通过的元素就返回true

set_2 = frozenset({1, 3, 5, 7})  # 不可变的集合,不可以删除和添加剩下的操作都一样
set_3 = frozenset(range(1, 6))
print(set_2, set_3)
print(set_1 & set_2)