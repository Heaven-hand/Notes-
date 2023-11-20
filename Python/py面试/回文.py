x = 121
z = str(x)
print(z)
y = list(z)
print(y.reverse())
if y.reverse() == y:
    print('yes')
else:
    print('no')