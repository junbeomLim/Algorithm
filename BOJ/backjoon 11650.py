N = int(input())
n = []
for i in range(N):
    n.append(list(map(int,input().split(' '))))
n.sort(key=lambda x: (x[0],x[1]))
for i in n:
    print(i[0],i[1])