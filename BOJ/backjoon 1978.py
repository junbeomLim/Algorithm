import math
N = int(input())
num = 0
n = [0 for i  in range(1000)]
n = list(map(int,input().split(' ')))
for i in range(0,N):
    if math.factorial(n[i]-1)%n[i] - n[i] == -1 and n[i] != 1:
        num = num + 1
print(num)