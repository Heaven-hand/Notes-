with open('文件名', 'rb') as file:
    a = file.read()

with open('新的文件名', 'wb') as file:
    file.write(a)
