T = int(input())
for k in range(T):
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split(' '))))
    A.sort(key=lambda x: x[0])
    a = A[0]
    count = 1
    for i in range(N):
        if a[1] > A[i][1]:
            a = A[i]
            count = count + 1
    print(count)