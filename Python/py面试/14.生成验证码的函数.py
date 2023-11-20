"""
整型数字和字目结合，可以指定长度
"""
import random


def code(num):
    res = ''
    for i in range(num):
        n = str(random.randint(0, 9))
        # 生成大写字母
        c = chr(random.randint(65, 90))
        # 生成小写字母
        d = chr(random.randint(65, 90)).lower()
        # 进行随机选择，参数是列表形式
        s = random.choice([n, c, d])
        # 65-90 A~Z  97~122 a~z
        res += s
    return res


print(code(6))
