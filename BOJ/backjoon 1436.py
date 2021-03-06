a = []
m = 5
for i in range(m):
    for j in range(10**i):
        for k in range(10**(m-i-1)):
            a.append((k*1000+666)*(10**i)+j)
a = list(set(a))
a.sort()
N = int(input())
print(a[N-1])