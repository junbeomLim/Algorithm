T = int(input())
for i in range(T):
    one = [0]
    zero = [1]
    N = int(input())
    for i in range(N+1):
        for j in range(i+1):
            zero[i] += zero[j]
    print(zero[N])
#zero[i] = zero[i-1]+zero[i-2]+....