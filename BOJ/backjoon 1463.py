N = int(input())
minimum = [0 for i in range(N+1)]
for i in range(2,N+1):
    if i%3 == 0:
        if i%2 == 0:
            minimum[i] = min(minimum[i-1]+1,minimum[int(i/3)]+1,minimum[int(i/2)]+1)
        else:
            minimum[i] = min(minimum[i-1]+1,minimum[int(i/3)]+1)
    elif i%2 == 0:
        minimum[i] = min(minimum[i-1]+1,minimum[int(i/2)]+1)
    else:
        minimum[i] = minimum[i-1]+1
print(minimum[N])