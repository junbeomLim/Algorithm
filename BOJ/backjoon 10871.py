N,X = map(int,input().split(' '))
n = [0 for i in range(N)]
n = list(map(int,input().split(' ')))
for i in n:
    if i < X:
        print(i,end=' ')