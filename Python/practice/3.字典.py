# 字典类型的数据是无顺序的，并且已键值对的方式进行存储  {key:value,...}
# 值可以用任何类型，但是键只能是字符串数字或者元组
bob = {'name': 'bob',
       'age': 18,
       'gender': True,
       'height': 1.75}
print(type(bob))
print(bob['name'])
# print(bob['address'])  不存在的键会进行报错
print(bob.get('address'))

print(bob.keys())
print(bob.values())
print(bob.items()) # 返回元组

# del bob['gender']
# print(bob.pop('age'))
print(bob)
print(bob.popitem())
bob.setdefault('age', 18)
bob.update(bob)
print(bob)

for k, v in bob.items():
    print(k, v)
for k in bob:
    print('%s : %s'% (k, bob[k]))



