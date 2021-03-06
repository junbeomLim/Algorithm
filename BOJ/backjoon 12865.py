N, K = map(int,input().split())
obj = []
DP = [[0 for j in range(K+1)] for k in range(N+1)]
for i in range(N):
    W,V = map(int,input().split())
    obj.append([W,V])
obj.sort(key = lambda x : -x[0])
for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= obj[i-1][0]:
            DP[i][j] = max(DP[i-1][j],DP[i-1][j-obj[i-1][0]]+obj[i-1][1])
for i in range(1,N+1):
    print(DP[i])
print(DP[N][K])