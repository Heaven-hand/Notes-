"""
求薪资最高的人的人名
"""
salaries = {
    'aaa': 300,
    'bbb': 2000,
    'ccc': 500
}
# print(salaries.values())
price = list(salaries.values())
price.sort()
for i in price:
    highest = i
for k in salaries:
    if salaries[k] == highest:
        print(k)

# res = max(salaries)  # 默认比较的是key
# print(res)


res = max(salaries, key=lambda name: salaries[name])  # 匿名函数

print(res)
