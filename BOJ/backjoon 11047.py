N, K = map(int,input().split(' '))
A = []
for i in range(N):
    A.append(int(input()))
count = 0
for i in range(N-1,-1,-1):
    count = count + K//A[i]
    K = K%A[i]
print(count)