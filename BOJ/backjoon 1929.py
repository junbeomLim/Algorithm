import math
M, N = map(int,input().split())
for i in range(M,N+1):
    if math.factorial(i-1)%i - i == -1 and i != 1:
        print(i)