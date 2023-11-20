"""
求集合的交集并集差集
"""

set1 = {2, 2.2, True, 4+3j}
set2 = {1, 2.2, False, 4+3j}
# 以第二个集合为优先
print(set1 & set2)  # intersection True is bool 1 依赖于set2，主动地把true变成1
print(set2 & set1)

# 以第一个集合为优先
print(set1 | set2)  # join
print(set2 | set1)

print(set1 - set2)  # set1 减去交集
print(set2 - set1)  # set2 减去交集
