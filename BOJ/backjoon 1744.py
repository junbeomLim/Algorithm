N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
a.sort()
count = 0
i = 0
while len(a) > 1 and i < len(a)-1:
    if a[i] >= 0:
        break
    if a[i] <= 0 and a[i+1] <= 0:
        A = a[i]*a[i+1]
        a.pop(i)
        a.pop(i)
        count = count + A
    else:
        i = i + 1
a.sort(key=lambda x: -x)
i = 0
while len(a) > 1 and i < len(a)-1:
    if a[i] < 0:
        break
    if a[i]*a[i+1] > a[i]+a[i+1]:
        A = a[i]*a[i+1]
        a.pop(i)
        a.pop(i)
        count = count + A
    else:
        i = i + 1
print(count + sum(a))