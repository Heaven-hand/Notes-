# 定义一个列表
name_list = ['a', 'b', 'c']
print(name_list)

# 在指定位置插入数据
name_list.insert(1, 'd')  # 在指定位置插入，之后的列表内容向后顺延
print(name_list)

# 在列表末尾添加一个数据
name_list.append('e')
print(name_list)

# 在指定位置修改元素
name_list[1] = 'b'
print(name_list)

# 删除指定的数据
del name_list[1]  # 会从内存中删除 后序无法继续使用，建议使用列表推荐的方法删除
print(name_list)

# 删除列表中的第一个出现的指定数据
name_list.remove('a')
print(name_list)

# pop 删除
name_list.pop()  # 不传数值默认删除最后一个数据
print(name_list)
name_list.pop(0)  # 添加索引可以删除索引数据
print(name_list)

# # 清楚整个列表
# name_list.clear()
# print(name_list)

# 统计
print(len(name_list))

# 统计元素出现的次数
print(name_list.count('c'))

# 列表的排序
number_list = [2, 4, 1, 5, 3, 6]
number_list.sort()  # 升序排列
print(number_list)

number_list.sort(reverse=True)  # 降序排列
print(number_list)

number_list.reverse()
print(number_list)  # 逆序，没有排序的效果

# 循环取值
for i in number_list:  # 列表中为str也可以取出
    print(i)
    print(type(i))

test1 = [1, 2, 3]
test2 = [4, 4, 3]
test1.extend(test2)  # 添加到后面
print(test1)


nums =[3,2,3,1,2,4,5,5,6]
k = 4
nums.sort()
print(nums)

nums_1 = list(set(nums))
print(nums_1)
nums_1.reverse()

print(nums_1)
print(nums_1[k-1])
a = 3
b = 4
c = (a>b and a or b)
print(c)