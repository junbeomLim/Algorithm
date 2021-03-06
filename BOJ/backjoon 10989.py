import sys
N = int(input())
n = [0 for i in range(10000)]
for i in range(N):
    a = int(sys.stdin.readline())
    n[a-1] = n[a-1] + 1
for i in range(10000):
    if n[i] != 0:
        for j in range(n[i]):
            sys.stdout.write(str(i+1)+'\n')
