alpabet = 'abcdefghijklmnopqrstuvwxyz'
n = input()
for i in alpabet:
    if n.count(i) >= 1:
        print(n.index(i),end=' ')
    else:
        print('-1',end=' ')