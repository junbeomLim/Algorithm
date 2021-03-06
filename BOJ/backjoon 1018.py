N, M = map(int, input().split(' '))
chass = []
mini = []
for i in range(N):
    chass.append(input())
for i in range(N-7):
    for j in range(M-7):
        x, y = 0,0
        for k in range(i,i+8):
            for w in range(j,j+8):
                if (k+w)%2 == 0:
                    if chass[k][w] != 'W':
                        x += 1
                    if chass[k][w] != 'B':
                        y += 1
                else:
                    if chass[k][w] != 'B':
                        x += 1
                    if chass[k][w] != 'W':
                        y += 1
        mini.append(x)
        mini.append(y)
print(min(mini))