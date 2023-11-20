# 定义一个元组类型的数据，元组的元素是不可以被修改的
info_data = (1, 'bob', 1.43)
print(type(info_data))

# 在声明一个元组类型的数据时，如果只有一个元素，必须在后面加一个，
info_data_1 = (1)
print(type(info_data_1))  # int类型的数据

info_data_2 = (1, )
print(type(info_data_2))

# 统计元组中的元素次数
info_data_3 = (1, 1, 2, 1, 4)
print(info_data_3.count(1))

# index是元组第一个该元素的下标
print(info_data_3.index(2))

for i in info_data:
    print(i)

# 转换数据的类型
print(type(list(info_data_3)))
print(type(tuple(info_data_3)))
