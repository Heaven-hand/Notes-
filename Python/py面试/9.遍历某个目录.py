"""
遍历
1.判断是文件还是文件夹
2.文件夹就继续
3.递归到没有文件夹
"""

import os


def func(path):
    list_path = os.listdir(path)  # 文件目录
    for i in list_path:  # 有列表就遍历
        full_path = os.path.join(path, i)  # 合并
        if os.path.isdir(full_path):
            func(full_path)  # 递归
        else:
            print(full_path)


path = r'D:\SteamLibrary'
func(path)
