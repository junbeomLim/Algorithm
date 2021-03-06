#f(n) = 1부터 n-1 까지 합
x = int(input())
memo = [0 for i in range(x+1)]
def f(n):
    if n == 1:
        memo[1] = 1
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = f(n-1) + n
    return memo[n]
print(f(x))