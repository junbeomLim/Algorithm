N = int(input())
n = []
for i in range(N):
    n.append(int(input()))
print(round(sum(n)/N))
n.sort()
print(n[(len(n)-1)//2])
a = []
for i in n:
    if a.count(i) < 1:
        a.append(i)
m = 0
for i in a:
    if n.count(i) > m:
        m = n.count(i)
b = []
for i in a:
    if n.count(i) == m:
        b.append(i)
if len(b) == 1:
    print(b[0])
else:
    b.sort()
    print(b[1])
print(max(n)-min(n))
