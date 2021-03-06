bang = [0,1,2,4,0,0,0,0,0,0,0,0]
T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(4,n+1):
        if bang[i] == 0:
            bang[i] = bang[i-1] + bang[i-2] + bang[i-3]
    print(bang[n])