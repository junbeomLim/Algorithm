N = int(input())
a = []
for i in range(N):
    a.append(list(map(int,input().split(' '))))
for i in range(N):
    k = 1
    for j in range(N):
        if j == i:
            continue
        elif a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            k = k + 1
    print(k)