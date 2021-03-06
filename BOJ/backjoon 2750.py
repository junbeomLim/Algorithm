N = int(input())
n = [0 for i in range(N)]
for i in range(N):
    n[i] = int(input())
n.sort()
for i in range(N):
    print(n[i])