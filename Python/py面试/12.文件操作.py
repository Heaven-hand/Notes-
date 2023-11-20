try:
    file = open('test.txt', 'r')
    f = file.read()
    print(f)
except Exception as error:
    file = open('test.txt', 'w')
    file.write('new file')
finally:
    file.close()