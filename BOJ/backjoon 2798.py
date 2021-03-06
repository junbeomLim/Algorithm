N, M = map(int,input().split(' '))
l = list(map(int,input().split(' ')))
L = []
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            L.append(l[i]+l[j]+l[k])
L.sort()
i = 0
a = False
for i in range(len(L)):
    if L[i] > M:
        a = True
        break
if a == True:
    print(L[i-1])
else:
    print(L[i])