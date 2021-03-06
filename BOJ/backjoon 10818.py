N = int(input())
n = [0 for i in range(N)]
n = list(map(int, input().split()))
print(min(n),max(n))