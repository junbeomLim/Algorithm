memo = [0 for i  in range(22)]
def pibo(N):
    if N == 0:
        memo[0] = 0
        return 0
    if N == 1:
        memo[1] = 1
        return 1
    if memo[N] != 0:
        return memo[N]
    else:
        memo[N] = pibo(N-1) + pibo(N-2)
        return memo[N]

n = int(input())
print(pibo(n))