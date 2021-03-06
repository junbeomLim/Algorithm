T = int(input())
for i in range(T):
    N,s = input().split(' ')
    R = int(N)
    for i in s:
        for j in range(R):
            print(i,end='')
    print()