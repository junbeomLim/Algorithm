N = int(input())
a = N//5
b = N//3
visit = []
for i in range(0,b+1):
    for j in range(0,a+1):
        if 3*i + 5*j == N:
            visit.append(i+j)
if visit == []:
    print(-1)
else:
    print(min(visit))